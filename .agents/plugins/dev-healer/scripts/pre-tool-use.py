import sys
import json
import re

def normalize_windows_path(raw_path):
    clean_path = raw_path.replace("\\", "/")
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
            if re.search(r"\b(rm\s+-rf|sudo|poweroff|reboot)\b", cmd):
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
        sys.stderr.write(f"PreToolUse Error: {e}\n")
        print(json.dumps({"decision": "allow", "reason": "Bypass on internal error."}))
        sys.exit(0)

if __name__ == '__main__':
    main()
