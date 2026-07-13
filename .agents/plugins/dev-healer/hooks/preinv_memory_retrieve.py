import json
import sys
import os
from pathlib import Path

def main():
    try:
        input_data = sys.stdin.read()
        payload = json.loads(input_data) if input_data else {}
    except Exception:
        payload = {}

    prompt = payload.get("prompt", "")
    
    # Try to read semantic patterns
    workspace_root = Path(os.environ.get("ANTIGRAVITY_WORKSPACE_ROOT", os.getcwd()))
    patterns_file = workspace_root / ".agents" / "memory" / "semantic" / "devhealer_patterns.md"
    
    injected_context = ""
    if patterns_file.exists():
        with open(patterns_file, "r") as f:
            patterns = f.read()
            if patterns:
                injected_context = f"\n[DEVHEALER CONTEXT]: Known semantic patterns for this workspace:\n{patterns}\n"
    
    response = {}
    if injected_context:
        # According to standard hook schema, we can inject messages
        response["inject_messages"] = [
            {
                "role": "system",
                "content": injected_context
            }
        ]
        
    print(json.dumps(response))

if __name__ == "__main__":
    main()
