import os
import sys
import subprocess
import json

def log(msg, error=False):
    stream = sys.stderr if error else sys.stdout
    stream.write(msg + "\n")
    stream.flush()

def init_git():
    log("=== Checking Git Status ===")
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True, check=True)
        log("[+] Active Git workspace detected.")
    except Exception:
        log("[!] Not a Git repository. Initializing Git to unlock 'New Worktree Mode' support...")
        try:
            subprocess.run(["git", "init"], check=True)
            with open("README.md", "w") as f:
                f.write("# DevHealer Active Workspace\n")
            subprocess.run(["git", "add", "README.md"], check=True)
            subprocess.run(["git", "commit", "-m", "Initial commit from DevHealer Setup"], check=True)
            log("[+] Git initialized and initial commit created successfully.")
        except Exception as e:
            log(f"[-] Failed to initialize Git: {e}", error=True)

def scaffold_directories():
    log("=== Scaffolding DevHealer MAPE-K Directories ===")
    dirs = [
        ".agents",
        ".agents/rules",
        ".agents/workflows",
        ".agents/skills/heal-and-evolve",
        ".agents/scripts",  # ALIGNED: Moved scripts inside .agents to resolve folder drift
        "sidecars/watcher"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        log(f"[+] Scaffolding directory: {d}")

def write_assets():
    log("=== Writing DevHealer Core Files ===")
    
    # 1. Standard flat hooks.json mapping (2.0 format)
    hooks_config = {
        "PreToolUse": [
            {
                "command": "python .agents/scripts/pre-tool-use.py",
                "timeout": 15
            }
        ],
        "PostToolUse": [
            {
                "command": "python .agents/scripts/post-tool-use.py",
                "timeout": 15
            }
        ],
        "Stop": [
            {
                "command": "python .agents/scripts/stop-handler.py",
                "timeout": 15
            }
        ]
    }
    with open(".agents/hooks.json", "w") as f:
        json.dump(hooks_config, f, indent=2)
    log("[+] Wrote flat hooks.json config.")

    # 2. Hardened Semantic Firewall with Path Normalization
    pre_tool_use = """import sys
import json
import re

def normalize_windows_path(raw_path):
    clean_path = raw_path.replace("\\\\", "/")
    if len(clean_path) >= 2 and clean_path == ":":
        clean_path = clean_path[2:]
    return clean_path

def main():
    try:
        payload = json.load(sys.stdin)
        tool_call = payload.get("toolCall", {})
        tool_name = tool_call.get("name")
        tool_args = tool_call.get("args", {})
        
        # Guard destructive host commands
        if tool_name == "run_command":
            cmd = tool_args.get("CommandLine", "")
            if re.search(r"\\b(rm\\s+-rf|sudo|poweroff|reboot)\\b", cmd):
                print(json.dumps({"decision": "deny", "reason": "Destructive operations are blocked."}))
                sys.exit(0)
                
        # Guard VCS metadata directories
        if tool_name in ["write_to_file", "replace_file_content", "multi_replace_file_content"]:
            target_path = normalize_windows_path(tool_args.get("TargetFile", ""))
            if ".git/" in target_path or ".ssh/" in target_path:
                print(json.dumps({"decision": "deny", "reason": "Modifying VCS directories is blocked."}))
                sys.exit(0)

        print(json.dumps({"decision": "allow", "reason": "Passed Semantic Firewall."}))
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"PreToolUse Error: {e}\\n")
        print(json.dumps({"decision": "allow", "reason": "Bypass on internal error."}))
        sys.exit(0)

if __name__ == '__main__':
    main()
"""
    with open(".agents/scripts/pre-tool-use.py", "w") as f:
        f.write(pre_tool_use)
    log("[+] Wrote .agents/scripts/pre-tool-use.py")

    # 3. Strict Mode Compliant Loop stop-handler.py
    stop_handler = """import sys
import json
import os

def main():
    try:
        payload = json.load(sys.stdin)
        
        # Enforce AppData state isolation. No workspace fallback permitted!
        data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
        if not data_dir:
            print(json.dumps({"decision": "stop"}))
            sys.exit(0)
            
        state_path = os.path.join(data_dir, "healing-state.json")
        if not os.path.exists(state_path):
            print(json.dumps({"decision": "stop"}))
            sys.exit(0)
            
        with open(state_path, "r") as f:
            state = json.load(f)
            
        if state.get("status") == "active" and state.get("retryCount", 0) < 3:
            state["retryCount"] = state.get("retryCount", 0) + 1
            with open(state_path, "w") as f:
                json.dump(state, f)
            print(json.dumps({
                "decision": "continue",
                "reason": f"Anomaly active. Retry {state['retryCount']}/3. Run /workflow-heal-project."
            }))
            sys.exit(0)
            
        print(json.dumps({"decision": "stop"}))
    except Exception as e:
        sys.stderr.write(f"Stop Hook Error: {e}\\n")
        print(json.dumps({"decision": "stop"}))

if __name__ == '__main__':
    main()
"""
    with open(".agents/scripts/stop-handler.py", "w") as f:
        f.write(stop_handler)
    log("[+] Wrote .agents/scripts/stop-handler.py")

if __name__ == '__main__':
    init_git()
    scaffold_directories()
    write_assets()
