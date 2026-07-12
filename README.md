# DevHealer Harness

The **DevHealer Harness** is an autonomous, self-healing diagnostic and loop-control wrapper built to standardize your daily coding with powerful, tightly integrated coding agents. It prevents recursive git loops, enforces a Strict Mode out-of-band state configuration, and uses an explicitly defined structural ontology.

## Repository Structure

The layout is strict to ensure the agent's scratchpad and state never clobber your working tree.

```text
ITS/ (Repository Root)
├── .gitignore                          # Excludes temporary worktrees, logs, and venv
├── README.md                           # Onboarding instructions & quickstart commands
├── devhealer_colab_notebook.ipynb      # Interactive installation & simulation notebook
├── master_operations_manual.md         # Single Source of Truth architectural spec
├── setup.py                            # The workspace-scaffolding installer script
├── run_tests_hardened.py               # Windows process-tree file-lock sweeper
├── test_harness.ps1                    # Powershell background diagnostic watcher
├── deploy_global.ps1                   # Global plugin promotion deployer
└── .agents/                            # Antigravity project customization folder
    ├── hooks.json                      # Flat 2.0 event-keyed hooks registration
    ├── mcp_config.json                 # Core sparse MCP server definitions
    ├── scripts/                        # Synchronous runtime interception hooks
    │   ├── pre-tool-use.py             # Semantic firewall & command-gating rules
    │   ├── post-tool-use.py            # Anomaly categorization state writer
    │   └── stop-handler.py             # Sliding retry & sliding loop controller
    ├── rules/                          # Prompt-level workspace constraints
    │   └── development-ontology.md     # Core MAPE-K taxonomy & rule constraints
    ├── workflows/                      # Trajectory-level slash commands
    │   ├── workflow_heal_project.md    # Sequential /workflow_heal_project trajectory
    │   └── workflow_evolve_rules.md    # Automated rule-compaction workflow
    └── skills/                         # Encapsulated task reasoning modules
        └── heal-and-evolve/            
            └── SKILL.md                # Diagnostic & remediation decision trees
```

## Quick Start

1. **Scaffold the Workspace**:
   Run `python setup.py` to initialize missing `.agents` directories and bind the core hooks.
   Alternatively, run the interactive steps in `devhealer_colab_notebook.ipynb`.

2. **Run Tests with Hardened Wrapper**:
   To prevent "Access is Denied" file locks on Windows during automated Git cleanup and rotation, *never run bare test commands natively*.
   Instead, use:
   ```bash
   python run_tests_hardened.py <command>
   ```

3. **Background Watcher**:
   Invoke the diagnostic watcher via `.\test_harness.ps1` to detect file disruptions and simulate agent proactive triggers.

## Strict Mode: State Storage

The loop's dynamic state (like anomaly triggers and sliding counters) is explicitly banned from being written to `.agents/scratch/`. All continuously changing sidecar state is pushed to the `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%` to prevent Git index dirtying and maintain absolute sandboxing.

## Auditing the Harness

To generate a precise, high-fidelity logic and security audit of the configuration without polluting the LLM context with binary blobs or verbose prose, run:
```bash
npx repomix --include "setup.py,run_tests_hardened.py,test_harness.ps1,.agents/hooks.json,.agents/mcp_config.json,.agents/scripts/**/*.py,.agents/rules/**/*.md,.agents/workflows/**/*.md,.agents/skills/**/*.md"
```
The resulting `repomix-output.xml` can be pasted straight into an auditor LLM.
