import sys
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
        sys.stderr.write(f"Stop Hook Error: {e}\n")
        print(json.dumps({"decision": "stop"}))

if __name__ == '__main__':
    main()
