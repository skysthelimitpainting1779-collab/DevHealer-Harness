# DevHealer Master Prompt Playbook
# Consolidated system control prompts for Antigravity 2.0 MAPE-K Loop

This playbook contains all the master prompts required to deploy, configure, secure, and operate your autonomic self-healing loop.

---

## Playbook 1: System DNA Audit Prompt
Use this prompt inside a fresh workspace or terminal session to extract absolute system details:

```text
Please execute a comprehensive system audit of our current Windows 10 development environment so we can gather the exact technical configurations required to build a production-hardened, self-healing loop. 

Please run the necessary terminal commands and file system checks to output a structured markdown report covering the following details:

1. PATHS & OS ENVIRONMENT:
   - What is the absolute path to this active workspace?
   - What are the absolute resolved paths for %USERPROFILE% and %APPDATA%?
   - Run 'git rev-parse --is-inside-work-tree' to confirm if this project folder is actively version-controlled.

2. PYTHON CONFIGURATION:
   - Test which executable successfully launches Python: run 'python --version', 'python3 --version', and 'py --version'.
   - Check if 'google-antigravity' is installed: 'pip show google-antigravity'.

3. DEVELOPER TOOLCHAIN & DATABASE:
   - Identify active files like package.json, requirements.txt, etc.
   - Run 'node -v' and 'npm -v' to check.
```

---

## Playbook 2: DevHealer Core Setup Prompt
Use this to trigger the initial compilation and directory generation script:

```text
Please help me bootstrap our production-hardened self-healing environment. I have downloaded and placed the "setup.py" script inside our workspace.

Please execute the following terminal tasks:
1. Install our Python SDK: pip install google-antigravity
2. Run the Installer: python setup.py
3. Confirm Environment Assets: Verify Git is initialized, and that .agents/ is fully populated with hooks.json, rules/, and skills/ folders.
```

---

## Playbook 3: Trajectory & Workflow Integration Prompt
Registers your `/workflow-heal-project` trajectory workflow:

```text
Please help me register our official autonomic self-healing trajectory workflow. I have provided you with "workflow_heal_project.md".

Please run the necessary tasks:
1. Save the file directly to .agents\workflows\workflow_heal_project.md.
2. Confirm run_tests_hardened.py is at workspace root.
3. Commit both files to Git to ensure worktree availability.
```

---

## Playbook 4: Strict Mode Hybrid Isolation Guard
Paste this rule directly to your active ruleset to prevent write blocks:

```text
[SYSTEM RULE: HYBRID SCOPE & LOCAL WRITE PROTECTION]
1. When performing the self-evolution (Knowledge) phase of our loop, you are strictly prohibited from writing or modifying files outside of your active workspace directory.
2. To avoid Strict Mode write-denials, always write newly evolved rules and skills locally inside .agents/rules/ and .agents/skills/ respectively. Do not write to global profiles.
```

---

## Playbook 5: Windows File-Locking Mitigation Guard
Ensures your agent manages process trees cleanly during branch changes:

```text
[SYSTEM RULE: SUBAGENT DELEGATION & PROCESS-TREE CLEANUP]
1. The platform enforces a hard nesting limit of 10 subagent levels. Do not exceed this boundary.
2. When running tests inside a Git worktree, you must prepend all commands with:
   python run_tests_hardened.py <command>
3. Confirm that all spawned processes are completely terminated before completing a subagent turn, preventing Windows "Access is denied" locking errors during worktree teardown.
```

---

## Playbook 6: Credentials & Telemetry Compliance Guard
Secures your API integration tokens and telemetry logs:

```text
[SYSTEM RULE: CREDENTIALS ISOLATION & TELEMETRY COMPLIANCE]
1. You are strictly forbidden from writing cleartext authentication tokens, passwords, or JWT keys into any git-tracked configuration file.
2. Always instruct the user to export secrets as local host environment variables (e.g., ENV_VAR_PROJECT_TURSO_TOKEN) and reference them dynamically inside config files.
```
