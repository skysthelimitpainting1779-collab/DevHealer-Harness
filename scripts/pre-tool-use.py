import sys
import json

def log(msg):
    sys.stderr.write(f"[Firewall Log] {msg}\n")

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
        normalized_target = target_file.replace("\\", "/").replace("\\", "/").lower()
        
        # Firewall matching constraints
        if ".git/" in normalized_target or ".git\\" in target_file:
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
