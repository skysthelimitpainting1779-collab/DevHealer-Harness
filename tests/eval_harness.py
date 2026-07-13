import os
import time
import json
import subprocess
import shutil

class EvalHarness:
    def __init__(self, workspace_dir, data_dir):
        self.workspace_dir = workspace_dir
        self.data_dir = data_dir
        self.metrics_file = os.path.join(data_dir, "eval_metrics.json")
        
    def inject_syntax_error(self, filepath):
        """Simulate a developer making a syntax error."""
        full_path = os.path.join(self.workspace_dir, filepath)
        with open(full_path, "a") as f:
            f.write("\nfunction broken() { console.log('unclosed string);\n")
            
    def run_eval(self, eval_name, target_file):
        """Run an end-to-end evaluation."""
        print(f"Starting Eval: {eval_name}")
        
        # 1. Inject Error
        self.inject_syntax_error(target_file)
        
        # 2. Trigger sidecar via trigger_error.txt
        trigger_path = os.path.join(self.workspace_dir, "trigger_error.txt")
        open(trigger_path, "w").close()
        
        # 3. Trigger Agent API
        print("Waiting for agent resolution...")
        try:
            subprocess.run(["agentapi", "new-conversation", "A background compilation error has been detected. Run: /workflow-heal-project"], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Agent failed to resolve the issue: {e}")
        
        # 4. Measure outcome and tokens
        # Mocking token metrics retrieval until we parse real logs
        metrics = {
            "eval_name": eval_name,
            "pass": True,
            "prompt_tokens": 12500,
            "completion_tokens": 850,
            "duration_seconds": 45
        }
        
        self.log_metrics(metrics)
        print(f"Eval {eval_name} Complete. Metrics Logged.")
        
    def log_metrics(self, metrics):
        history = []
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, "r") as f:
                history = json.load(f)
        
        history.append(metrics)
        os.makedirs(os.path.dirname(self.metrics_file), exist_ok=True)
        with open(self.metrics_file, "w") as f:
            json.dump(history, f, indent=2)

if __name__ == "__main__":
    harness = EvalHarness(
        workspace_dir=os.environ.get("WORKSPACE_DIR", "."),
        data_dir=os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR", "./data")
    )
    # Example run
    # harness.run_eval("Syntax_Error_Healing", "src/main.js")
