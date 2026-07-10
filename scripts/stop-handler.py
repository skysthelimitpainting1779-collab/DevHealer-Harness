import sys
import json
import os

def log(msg):
    sys.stderr.write(f"[LoopControl Log] {msg}\n")

def main():
    try:
        input_data = json.load(sys.stdin)
        log("Sensing Stop checkpoint rules.")
        
        data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
        if not data_dir:
            user_profile = os.environ.get("USERPROFILE", "C:\\Users\\Johnny Cage")
            data_dir = os.path.join(user_profile, ".gemini", "antigravity", "sidecar_data", "dev-healer", "data")
        
        state_path = os.path.join(data_dir, "healing-state.json")
        
        decision = "allow"
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
        sys.stdout.write(json.dumps({"decision": "allow"}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
