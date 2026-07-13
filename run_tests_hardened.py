import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_tests_hardened.py <command>")
        sys.exit(1)
        
    command = sys.argv[1:]
    print(f"Running hardened wrapper for: {' '.join(command)}")
    
    # Run the command and capture output
    try:
        result = subprocess.run(command, text=True, capture_output=True)
    except FileNotFoundError:
        print(f"Command not found: {command[0]}")
        sys.exit(1)
        
    # Output the result to the console so the user sees it
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    
    # If the command failed, write to the devhealer_error.log for the sidecar to catch
    if result.returncode != 0:
        data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
        if not data_dir:
            user_profile = os.environ.get("USERPROFILE", os.path.expanduser("~"))
            data_dir = os.path.join(user_profile, ".gemini", "antigravity", "sidecar_data", "dev-healer", "data")
            
        error_log_path = os.path.join(data_dir, "devhealer_error.log")
        os.makedirs(os.path.dirname(error_log_path), exist_ok=True)
        
        with open(error_log_path, "w") as f:
            f.write(f"\n--- ANOMALY DETECTED ---\n")
            f.write(f"Command: {' '.join(command)}\n")
            f.write(f"Exit Code: {result.returncode}\n")
            f.write(f"Stderr:\n{result.stderr}\n")
            
        print(f"\n[DevHealer] Hardened Wrapper caught non-zero exit code ({result.returncode}). Logged to {error_log_path}")
        
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
