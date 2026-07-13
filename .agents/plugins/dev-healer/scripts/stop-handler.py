import sys
import json
import os

def main():
    try:
        payload = json.load(sys.stdin)
        
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
            
        # Circuit Breaker: Force loop re-entry if the crash is unresolved
        if state.get("status") == "active" and state.get("retryCount", 0) < 3:
            state["retryCount"] = state.get("retryCount", 0) + 1
            with open(state_path, "w") as f:
                json.dump(state, f)
                
            # Intercept stop and force loop re-entry
            print(json.dumps({
                "decision": "continue",
                "reason": "An active software crash has been detected. Run /workflow-heal-project to repair."
            }))
            sys.exit(0)
            
        # Allow clean stop if the error is resolved or max retries are breached
        print(json.dumps({"decision": "stop"}))
    except Exception as e:
        sys.stderr.write(f"Stop Hook Error: {e}\n")
        print(json.dumps({"decision": "stop"}))

if __name__ == '__main__':
    main()
