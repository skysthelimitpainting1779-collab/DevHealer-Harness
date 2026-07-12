import sys
import json
import os

def log(msg):
    sys.stderr.write(f"[Sensation Log] {msg}\n")

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
                user_profile = os.environ.get("USERPROFILE", "C:\\Users\\Johnny Cage")
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
