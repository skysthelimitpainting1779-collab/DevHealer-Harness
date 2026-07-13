import os
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Create a FastMCP server
mcp = FastMCP("DevHealer Brain")

# Resolve the memory directory relative to the workspace root
# We assume this script runs in the context of the workspace
WORKSPACE_ROOT = Path(os.environ.get("ANTIGRAVITY_WORKSPACE_ROOT", os.getcwd()))
MEMORY_DIR = WORKSPACE_ROOT / ".agents" / "memory"

@mcp.tool()
def search_past_failures(error_message: str) -> str:
    """
    Search the episodic memory graph for past failures similar to the given error_message.
    """
    episodic_dir = MEMORY_DIR / "episodic"
    if not episodic_dir.exists():
        return "No episodic memory found."
    
    results = []
    # Very basic search for demonstration: grep through episodic logs
    for log_file in episodic_dir.glob("*.json"):
        try:
            with open(log_file, "r") as f:
                data = json.load(f)
                # If error message keywords are in the failure reason or context
                if any(word.lower() in str(data).lower() for word in error_message.split() if len(word) > 4):
                    results.append(f"Match found in {log_file.name}: {data.get('failure_reason', 'Unknown error')}")
        except Exception:
            pass

    if results:
        return "\n".join(results)
    return "No similar past failures found."

@mcp.tool()
def read_semantic_patterns() -> str:
    """
    Read the current codified semantic patterns and project rules.
    """
    patterns_file = MEMORY_DIR / "semantic" / "devhealer_patterns.md"
    if patterns_file.exists():
        with open(patterns_file, "r") as f:
            return f.read()
    return "No semantic patterns codified yet."

@mcp.tool()
def propose_new_rule(rule_text: str, context: str) -> str:
    """
    Propose a new rule or pattern based on a recently solved problem.
    """
    proposals_dir = MEMORY_DIR / "metadata" / "proposals"
    proposals_dir.mkdir(parents=True, exist_ok=True)
    
    proposal_file = proposals_dir / f"proposal_{hash(rule_text)}.json"
    with open(proposal_file, "w") as f:
        json.dump({"rule": rule_text, "context": context, "status": "pending_review"}, f, indent=2)
    
    return f"Rule proposed and saved to {proposal_file.name} for curation."

if __name__ == "__main__":
    mcp.run(transport="stdio")
