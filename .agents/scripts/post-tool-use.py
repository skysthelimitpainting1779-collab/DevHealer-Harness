import sys
import json
import os

def main():
    try:
        # 1. Read input payload from Antigravity stdin
        input_data = json.load(sys.stdin)
        error_msg = input_data.get("error", "")
        
        # 2. Resolve secure AppData path
        data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
        if not data_dir:
            print("{}")
            sys.exit(0)
            
        state_file = os.path.join(data_dir, "healing-state.json")
        
        # 3. If a tool call actually failed, write the real error to disk
        if error_msg:
            state = {}
            if os.path.exists(state_file):
                try:
                    with open(state_file, "r") as f:
                        state = json.load(f)
                except Exception:
                    pass
            
            # Save the raw crash details captured directly from the execution tool
            state["activeAnomaly"] = "ToolFailure"
            state["errorDetails"] = error_msg
            state["status"] = "active"
            state["retryCount"] = state.get("retryCount", 0)
            
            os.makedirs(data_dir, exist_ok=True)
            with open(state_file, "w") as f:
                json.dump(state, f, indent=2)
                
        # Return empty JSON to conform to PostToolUse contract
        print("{}")
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"PostToolUse Hook Error: {e}\n")
        print("{}")
        sys.exit(0)

if __name__ == "__main__":
    main()
