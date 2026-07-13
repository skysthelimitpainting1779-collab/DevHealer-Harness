import os
import glob
import re

def test_rule_character_limits():
    """Verify no rule file exceeds 12,000 characters."""
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    agents_dir = os.path.join(workspace_root, ".agents")
    rules_dir = os.path.join(agents_dir, "rules")
    
    if not os.path.exists(rules_dir):
        return
        
    for filename in os.listdir(rules_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(rules_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                assert len(content) <= 12000, f"Rule {filename} exceeds 12,000 characters."

def test_rule_frontmatter():
    """Verify rule files have required YAML frontmatter."""
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rules_dir = os.path.join(workspace_root, ".agents", "rules")
    
    if not os.path.exists(rules_dir):
        return
        
    for filename in os.listdir(rules_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(rules_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Basic YAML frontmatter extraction
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            assert match, f"Rule {filename} is missing YAML frontmatter."
            
            frontmatter = match.group(1)
            assert "trigger:" in frontmatter, f"Rule {filename} missing 'trigger' key."
            assert "description:" in frontmatter, f"Rule {filename} missing 'description' key."

def test_workflow_frontmatter():
    """Verify workflow files have required YAML frontmatter."""
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    workflows_dir = os.path.join(workspace_root, ".agents", "workflows")
    
    if not os.path.exists(workflows_dir):
        return
        
    for filename in os.listdir(workflows_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(workflows_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            assert match, f"Workflow {filename} is missing YAML frontmatter."
            
            frontmatter = match.group(1)
            assert "name:" in frontmatter, f"Workflow {filename} missing 'name' key."
            assert "description:" in frontmatter, f"Workflow {filename} missing 'description' key."
