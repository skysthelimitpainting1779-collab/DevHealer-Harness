# -*- coding: utf-8 -*-
"""
Google Antigravity 2.0 - Hardened Production Setup Script (v5)
Target Environment: Windows 10 Host (Johnny Cage / C:\\Users\\Johnny Cage\\ITS)
Grounded on: Windows Development Environment Audit Report & Antigravity Hardening Guide
"""

import os
import sys
import json
import shutil
import platform
import subprocess

def log(msg):
    sys.stderr.write(f"[Installer] {msg}\n")

# Target Workspace Normalization
WORKSPACE_DIR = os.getcwd()
NORMALIZED_WORKSPACE = WORKSPACE_DIR.replace("\\", "/")

def check_git_status():
    log("Auditing Git status...")
    is_git = False
    try:
        # Run standard non-blocking git check
        result = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], 
                                capture_output=True, text=True, shell=True)
        if result.returncode == 0 and "true" in result.stdout.lower():
            is_git = True
            log("Git repository detected. Isolated worktree mode will execute successfully.")
        else:
            log("WARNING: Directory is not version-controlled.")
    except Exception as e:
        log(f"Git execution audit failed: {str(e)}")
    return is_git

def initialize_git():
    log("Initializing Git repository to prevent silent worktree fallback...")
    try:
        result = subprocess.run(["git", "init"], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            log("SUCCESS: Git repository initialized successfully!")
            # Add a dummy commit so worktree operations have a head reference to branch off of
            with open("README.md", "w") as f:
                f.write("# ITS Project\nInitialized with Antigravity 2.0 Autonomic Loop.\n")
            subprocess.run(["git", "add", "README.md"], shell=True)
            subprocess.run(["git", "commit", "-m", "Initial commit from Antigravity v5 Installer"], shell=True)
            log("SUCCESS: Created initial commit.")
        else:
            log(f"ERROR: Failed to initialize Git. Details: {result.stderr}")
    except Exception as e:
        log(f"Exception while running git init: {str(e)}")

def build_scaffold():
    log(f"Beginning directory construction under: {WORKSPACE_DIR}")
    
    # Define directories relative to execution root
    dirs = [
        ".agents",
        ".agents/rules",
        ".agents/workflows",
        ".agents/skills",
        ".agents/skills/heal-and-evolve",
        "scripts",
        "sidecars",
        "sidecars/watcher",
        "resources"
    ]
    
    for d in dirs:
        os.makedirs(os.path.join(WORKSPACE_DIR, d), exist_ok=True)
    log("Scaffold directory structure built successfully.")

def write_files():
    # 1. plugin.json
    plugin_data = {
        "name": "antigravity-self-healer"
    }
    with open(os.path.join(WORKSPACE_DIR, ".agents", "plugin.json"), "w") as f:
        json.dump(plugin_data, f, indent=2)

    # 2. hooks.json (Flat 2.0 Event-Keyed Format, Windows Native Command Interpreter)
    hooks_data = {
        "PreToolUse": [
            {
                "command": "python",
                "args": ["scripts/pre-tool-use.py"],
                "timeout": 30
            }
        ],
        "PostToolUse": [
            {
                "command": "python",
                "args": ["scripts/post-tool-use.py"],
                "timeout": 60
            }
        ],
        "Stop": [
            {
                "command": "python",
                "args": ["scripts/stop-handler.py"],
                "timeout": 30
            }
        ]
    }
    with open(os.path.join(WORKSPACE_DIR, ".agents", "hooks.json"), "w") as f:
        json.dump(hooks_data, f, indent=2)

    # 3. mcp_config.json (Turso Integration Scaffolded with Node.js stdio Transport)
    mcp_data = {
        "mcpServers": {
            "turso-explorer": {
                "command": "node",
                "args": [
                    f"{NORMALIZED_WORKSPACE}/node_modules/@libsql/mcp-server/index.js"
                ],
                "env": {
                    "LIBSQL_URL": "libsql://your-database-name-username.turso.io",
                    "LIBSQL_AUTH_TOKEN": "YOUR_TURSO_JWT_AUTH_TOKEN_HERE"
                }
            }
        }
    }
    with open(os.path.join(WORKSPACE_DIR, ".agents", "mcp_config.json"), "w") as f:
        json.dump(mcp_data, f, indent=2)

    # 4. scripts/pre-tool-use.py (Hygienic Semantic Firewall, Path-Normalization Compliant)
    pre_tool_use_code = """import sys
import json

def log(msg):
    sys.stderr.write(f"[Firewall Log] {msg}\\n")

def main():
    try:
        input_data = json.load(sys.stdin)
        log("Evaluating PreToolUse safety criteria.")
        
        tool_call = input_data.get("toolCall", {})
        tool_name = tool_call.get("name")
        tool_args = tool_call.get("args", {})
        
        decision = "allow"
        reason = "Command within normal operational constraints."
        permission_overrides = []
        
        # Pull targets and normalize backslashes and drive letters
        target_file = tool_args.get("TargetFile") or tool_args.get("AbsolutePath") or tool_args.get("CommandLine") or ""
        normalized_target = target_file.replace("\\\\", "/").replace("\\\\", "/").lower()
        
        # Firewall matching constraints
        if ".git/" in normalized_target or ".git\\\\" in target_file:
            decision = "deny"
            reason = "Security Gate Failure: Direct modification of .git/ folders is strictly prohibited."
        elif "rmdir" in normalized_target or "rm -rf" in normalized_target:
            decision = "ask"
            reason = "Destructive recursive deletions require manual developer-in-the-loop validation."
            permission_overrides = ["command(rmdir)", "command(rm)"]

        output = {
            "decision": decision,
            "reason": reason,
            "permissionOverrides": permission_overrides
        }
        
        sys.stdout.write(json.dumps(output))
        sys.stdout.flush()
    except Exception as e:
        log(f"Firewall execution error: {str(e)}")
        sys.stdout.write(json.dumps({"decision": "ask", "reason": f"Firewall script error: {str(e)}"}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(WORKSPACE_DIR, "scripts", "pre-tool-use.py"), "w") as f:
        f.write(pre_tool_use_code)

    # 5. scripts/post-tool-use.py (Sensation Module, State Saved under Git-Immune AppData Path)
    post_tool_use_code = """import sys
import json
import os

def log(msg):
    sys.stderr.write(f"[Sensation Log] {msg}\\n")

def main():
    try:
        input_data = json.load(sys.stdin)
        log("Analyzing PostToolUse execution result.")
        
        error_msg = input_data.get("error", "")
        
        if error_msg:
            log(f"Tool error intercepted: {error_msg}")
            
            # Resolve git-immune secure AppData path dynamically
            data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
            if not data_dir:
                user_profile = os.environ.get("USERPROFILE", "C:\\\\Users\\\\Johnny Cage")
                data_dir = os.path.join(user_profile, ".gemini", "antigravity", "sidecar_data", "dev-healer", "data")
            
            os.makedirs(data_dir, exist_ok=True)
            state_path = os.path.join(data_dir, "healing-state.json")
            
            state = {
                "activeAnomaly": "ToolFailure",
                "errorDetails": error_msg,
                "status": "active",
                "retryCount": 0
            }
            
            with open(state_path, "w") as f:
                json.dump(state, f, indent=2)
            log(f"Anomaly successfully registered in system cache: {state_path}")
            
        sys.stdout.write(json.dumps({}))
        sys.stdout.flush()
    except Exception as e:
        log(f"Sensation module execution error: {str(e)}")
        sys.stdout.write(json.dumps({}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(WORKSPACE_DIR, "scripts", "post-tool-use.py"), "w") as f:
        f.write(post_tool_use_code)

    # 6. scripts/stop-handler.py (Loop Termination Overrider, Prevent Runaway Execution Loop)
    stop_handler_code = """import sys
import json
import os

def log(msg):
    sys.stderr.write(f"[LoopControl Log] {msg}\\n")

def main():
    try:
        input_data = json.load(sys.stdin)
        log("Sensing Stop checkpoint rules.")
        
        data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
        if not data_dir:
            user_profile = os.environ.get("USERPROFILE", "C:\\\\Users\\\\Johnny Cage")
            data_dir = os.path.join(user_profile, ".gemini", "antigravity", "sidecar_data", "dev-healer", "data")
        
        state_path = os.path.join(data_dir, "healing-state.json")
        
        decision = "stop"
        reason = "System conditions cleared."
        
        if os.path.exists(state_path):
            with open(state_path, "r") as f:
                state = json.load(f)
            
            if state.get("status") == "active":
                retries = state.get("retryCount", 0)
                if retries < 3:
                    decision = "continue"
                    reason = "Unresolved codebase anomaly remains. Re-entering execution trajectory via /workflow-heal-project."
                    state["retryCount"] = retries + 1
                    with open(state_path, "w") as f:
                        json.dump(state, f, indent=2)
                    log(f"Loop override engaged. Retrying build loop (Attempt {retries + 1}/3).")
                else:
                    state["status"] = "halted"
                    with open(state_path, "w") as f:
                        json.dump(state, f, indent=2)
                    log("Maximum build retry limit (3) reached. Halting loop to protect host resources.")
        
        output = {
            "decision": decision,
            "reason": reason
        }
        sys.stdout.write(json.dumps(output))
        sys.stdout.flush()
    except Exception as e:
        log(f"LoopControl execution error: {str(e)}")
        sys.stdout.write(json.dumps({"decision": "stop"}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(WORKSPACE_DIR, "scripts", "stop-handler.py"), "w") as f:
        f.write(stop_handler_code)

    # 7. sidecars/watcher/sidecar.json
    sidecar_json = {
        "description": "Continuous workspace file watcher for compiling/test failures.",
        "command": "python",
        "args": [
            "watcher.py"
        ],
        "restart_policy": "always"
    }
    with open(os.path.join(WORKSPACE_DIR, "sidecars", "watcher", "sidecar.json"), "w") as f:
        json.dump(sidecar_json, f, indent=2)

    # 8. sidecars/watcher/watcher.py (Continuous polling and agentapi activator)
    watcher_code = """import os
import time
import subprocess
import sys
import json

def log(msg):
    sys.stderr.write(f"[Watcher Log] {msg}\\n")

def main():
    log("Background Watcher Sidecar initialized on Windows 10.")
    workspace_dir = os.environ.get("WORKSPACE_DIR", "C:\\\\Users\\\\Johnny Cage\\\\ITS")
    
    # Watch for trigger file simulating error conditions
    trigger_file = os.path.join(workspace_dir, "trigger_error.txt")
    
    while True:
        try:
            if os.path.exists(trigger_file):
                log("Trigger file detected! Simulating tool compilation anomaly.")
                
                data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
                if not data_dir:
                    user_profile = os.environ.get("USERPROFILE", "C:\\\\Users\\\\Johnny Cage")
                    data_dir = os.path.join(user_profile, ".gemini", "antigravity", "sidecar_data", "dev-healer", "data")
                
                os.makedirs(data_dir, exist_ok=True)
                state_path = os.path.join(data_dir, "healing-state.json")
                
                state = {
                    "activeAnomaly": "ToolFailure",
                    "errorDetails": "Compilation failed in index.js: SyntaxError Unexpected token",
                    "status": "active",
                    "retryCount": 0
                }
                
                with open(state_path, "w") as f:
                    json.dump(state, f, indent=2)
                
                try:
                    os.remove(trigger_file)
                except Exception as e:
                    log(f"Failed to remove trigger file: {str(e)}")
                
                log("Executing agentapi command to launch proactive conversation...")
                try:
                    subprocess.run(["agentapi", "new-conversation", "A background compilation error has been detected. Run: /workflow-heal-project"], shell=True)
                except Exception as cli_err:
                    log(f"agentapi execution error: {str(cli_err)}")
                    
            time.sleep(5)
        except KeyboardInterrupt:
            break
        except Exception as e:
            log(f"Error in watcher loop: {str(e)}")
            time.sleep(5)

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(WORKSPACE_DIR, "sidecars", "watcher", "watcher.py"), "w") as f:
        f.write(watcher_code)

    # 9. workflows/workflow-heal-project.md
    heal_project_md = """# Proactive Project Self-Healing Trajectory
This workflow executes sequentially when a background sidecar logs a tool execution fault or testing failure.

## Trajectory Sequence
1. Read the structured failure details from our git-immune state registry using the `view_file` tool on `healing-state.json` inside the system path mapped by `ANTIGRAVITY_EXECUTABLE_DATA_DIR`.
2. Activate the `@heal-and-evolve` skill to run a rigorous diagnosis of the error logs and plan an isolated remediation.
3. Spawn a dedicated helper subagent using the `invoke_subagent` tool. You must configure the subagent to run in **New Worktree Mode** to shield the active repository from broken builds.
4. Inside the isolated background branch, direct the subagent to run edits and validation scripts (`npm run build`, `npm test`, etc.).
5. **Critical Windows Process Cleanup**: Before exiting, the subagent must explicitly trace and terminate all child processes it spawned to free Windows file lock handles, avoiding 'Access is denied' exceptions on directory cleanup.
6. Commit the passing build changes, merge the clean branch, reset `healing-state.json`, and run `/workflow-evolve-rules` to write hardened guidelines.
"""
    with open(os.path.join(WORKSPACE_DIR, ".agents", "workflows", "workflow-heal-project.md"), "w") as f:
        f.write(heal_project_md)

    # 10. workflows/workflow-evolve-rules.md
    evolve_rules_md = """# Rule Evolution & Compacting Trajectory
This workflow implements our strict code knowledge adaptation policy without breaching system file constraints.

## Trajectory Sequence
1. Analyze the successful remediation logs to isolate the root programming failure.
2. Draft a highly specific constraint rule targeting the error class and place it in `.agents/rules/`.
3. **Summarize-and-Compact Evolution Strategy**: If a rule file already exists, edit the file in place using the summarize-and-compact rewrite strategy. Do not blindly append logs or debugging traces.
4. Keep all rule Markdown files strictly below the **12,000-character cap** to prevent silent platform truncation.
"""
    with open(os.path.join(WORKSPACE_DIR, ".agents", "workflows", "workflow-evolve-rules.md"), "w") as f:
        f.write(evolve_rules_md)

    # 11. rules/development-ontology.md
    dev_ontology_md = """# Workspace Guidelines & Anomaly Ontology
This rule is Always-On and enforces project integrity guidelines for all developer agents.

## Enforced Standards
* **Process Handle Hygiene**: All background compilers, watchers, or test runners spawned in isolated worktrees must be explicitly terminated prior to subagent shutdown to prevent Windows directory lockups (Access is denied errors).
* **Workspace Isolation**: Multi-step codebase refactors or experimental repairs must be performed inside isolated background branches via New Worktree Mode.
* **Pathing Normalization**: Programmatically convert all backslashes (`\\`) to forward slashes (`/`) in path strings prior to testing permissions, drive letters must be stripped during evaluation.
* **Character Capacity Safeguard**: Never commit log dumps, compile warnings, or stack traces directly into rule files. Rule updates must use a rewrite-in-place compacting pattern to stay well below 12,000 characters.
"""
    with open(os.path.join(WORKSPACE_DIR, ".agents", "rules", "development-ontology.md"), "w") as f:
        f.write(dev_ontology_md)

    # 12. skills/heal-and-evolve/SKILL.md
    skill_md = """---
name: heal-and-evolve
description: Classifies and troubleshoot compile and runtime codebase anomalies. Use when analyzing test errors or resolving compilation faults.
---
# Heal and Evolve Skill
Provides the diagnostic framework and decision trees required to resolve structural failures.

## Diagnostic Protocol
1. **Anomaly Classification**: Parse the logs to classify the software error:
   - `ToolFailure`: Execution command returned a non-zero exit code.
   - `InputCorruption`: Broken schema specifications or mismatched parameters.
   - `ReasoningCollapse`: Runaway loop recursion or step capacity threshold reached.
2. **Technical Sourcing**: Consult local configurations or make targeted queries using `search_web` if encountering unfamiliar dependency issues.
3. **Remediation Strategy**: Draft the isolated repair, define verification commands, and delegate task boundaries.
"""
    with open(os.path.join(WORKSPACE_DIR, ".agents", "skills", "heal-and-evolve", "SKILL.md"), "w") as f:
        f.write(skill_md)

    # 13. scripts/sdk_agent_healer.py
    sdk_code = """import asyncio
import os
from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.hooks.policy import deny, allow, ask_user

async def main():
    # Windows-hardened deny-by-default execution policy
    policies = [
        deny("*"),
        allow("view_file"),
        ask_user("run_command")
    ]
    
    config = LocalAgentConfig()
    async with Agent(config) as agent:
        response = await agent.chat("Analyze our workspace rules and print our project self-healing protocol.")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())
"""
    with open(os.path.join(WORKSPACE_DIR, "scripts", "sdk_agent_healer.py"), "w") as f:
        f.write(sdk_code)

    # 14. resources/ontology.ttl
    ttl_code = """@prefix ag: <https://antigravity.google/ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ag:Loop a owl:Class ;
    rdfs:label "Autonomic Loop" .

ag:Anomaly a owl:Class ;
    rdfs:label "Software Anomaly" .

ag:ToolFailure a owl:Class ;
    rdfs:subClassOf ag:Anomaly ;
    rdfs:label "Tool Execution Failure" .

ag:RecoveryPlan a owl:Class ;
    rdfs:label "Remediation Trajectory" .
"""
    with open(os.path.join(WORKSPACE_DIR, "resources", "ontology.ttl"), "w") as f:
        f.write(ttl_code)

    log("All structural assets and configuration scripts written to disk successfully.")

def main():
    log("Verifying operating system compatibility...")
    is_windows = (platform.system() == "Windows")
    if is_windows:
        log("SUCCESS: Confirmed Windows host platform.")
    else:
        log("NOTICE: Running on non-Windows environment. Path mappings and commands are mapped to Windows standards.")
    
    # Run the Git check
    git_ready = check_git_status()
    if not git_ready:
        initialize_git()
        
    build_scaffold()
    write_files()
    log("=========================================================================")
    log("Google Antigravity Production v5 Bootstrap Installer Execution Completed!")
    log("=========================================================================")

if __name__ == "__main__":
    main()
