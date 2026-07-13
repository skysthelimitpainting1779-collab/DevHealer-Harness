import os
import json
import csv

def generate_report(data_dir):
    """Aggregate token effectiveness and measurable scoring from evals."""
    metrics_file = os.path.join(data_dir, "eval_metrics.json")
    report_file = os.path.join(data_dir, "eval_metrics_report.csv")
    
    if not os.path.exists(metrics_file):
        print(f"No metrics found at {metrics_file}")
        return
        
    with open(metrics_file, "r") as f:
        history = json.load(f)
        
    print("\n--- DevHealer Eval Metrics Report ---")
    
    with open(report_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Eval Name", "Status", "Prompt Tokens", "Completion Tokens", "Total Tokens", "Token Effectiveness (TE)", "Duration (s)"])
        
        for run in history:
            total_tokens = run["prompt_tokens"] + run["completion_tokens"]
            # Token Effectiveness (TE) score: 
            # 1.0 (Pass) or 0.0 (Fail) divided by thousands of tokens.
            # E.g., Pass (1) with 10k tokens = 0.1 TE Score. Higher is better.
            te_score = (1.0 if run["pass"] else 0.0) / (total_tokens / 1000.0) if total_tokens > 0 else 0
            
            writer.writerow([
                run["eval_name"],
                "PASS" if run["pass"] else "FAIL",
                run["prompt_tokens"],
                run["completion_tokens"],
                total_tokens,
                f"{te_score:.4f}",
                run["duration_seconds"]
            ])
            
            print(f"[{run['eval_name']}] Status: {'PASS' if run['pass'] else 'FAIL'}, TE Score: {te_score:.4f} (Tokens: {total_tokens})")

    print(f"\nDetailed CSV report written to: {report_file}")

if __name__ == "__main__":
    data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR", "./data")
    generate_report(data_dir)
