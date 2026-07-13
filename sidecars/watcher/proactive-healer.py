import os
import time
import subprocess
import sys
import json

def log(msg):
    sys.stderr.write(f"[Watcher Log] {msg}\n")

def main():
    log("Background Watcher Sidecar initialized on Windows 10.")
    workspace_dir = os.environ.get("WORKSPACE_DIR", "C:\\Users\\Johnny Cage\\ITS")
    
    # Watch for trigger file simulating error conditions
    trigger_file = os.path.join(workspace_dir, "trigger_error.txt")
    
    while True:
        try:
            if os.path.exists(trigger_file):
                log("Trigger file detected! Simulating tool compilation anomaly.")
                
                data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
                if not data_dir:
                    user_profile = os.environ.get("USERPROFILE", "C:\\Users\\Johnny Cage")
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
