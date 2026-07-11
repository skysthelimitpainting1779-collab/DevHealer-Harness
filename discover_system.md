# DevHealer System DNA Audit & Discovery Prompt

Please execute a comprehensive system audit of our current Windows 10 development environment so we can gather the exact technical configurations required to build a production-hardened, self-healing loop. 

Please run the necessary terminal commands and file system checks to output a structured markdown report covering the following details:

## 1. PATHS & OS ENVIRONMENT:
*   What is the absolute path to this active workspace? (Verify if it contains a drive letter like C:\ and print it).
*   What are the absolute resolved paths for %USERPROFILE% and %APPDATA% on this machine?
*   Run a quick terminal check to see if git is globally available, and run 'git rev-parse --is-inside-work-tree' to confirm if this project folder is actively version-controlled.

## 2. PYTHON CONFIGURATION:
*   Test which executable command successfully launches Python on this system: run 'python --version', 'python3 --version', and 'py --version'. Which one is active and what is the exact version?
*   Check if the Google Antigravity SDK is already installed in the active environment by running 'pip show google-antigravity'.

## 3. PROJECT ID & ANTIMETAL CONFIGS:
*   Scan our active environment variables or search ~/.gemini/config/config.json if it exists. What is the active projectId or folder configuration associated with this project?

## 4. DEVELOPER TOOLCHAIN:
*   Identify the programming language(s) and framework(s) used in this workspace (e.g., is there a package.json, requirements.txt, pyproject.toml, or cargo.toml?).
*   What are the exact local commands used to:
    a) Compile/build the project (e.g., 'npm run build', 'dotnet build', 'python -m compileall .')?
    b) Run the unit test suite (e.g., 'npm test', 'pytest', 'cargo test')?
    c) Run the code linter (e.g., 'eslint', 'flake8', 'pylint')?

## 5. TURSO / DATABASE CONFIGURATION:
*   Do we have Node.js and npm installed globally? Run 'node -v' and 'npm -v' to check.
*   Do you see any local configuration files related to Turso or SQLite? 
*   Is there an active remote Turso database URL (e.g., 'libsql://...') we should pre-bind to our local MCP configuration?

## 6. CURRENT CONFIGURATION DIRECTORIES:
*   Check if there are any existing customization folders in the project root: does .agents/ or the legacy .agent/ folder already exist? If so, what subdirectories (.agents/rules, .agents/workflows, .agents/skills) are present?

Once you have gathered this information, output it in a clean, structured Markdown table and list format so I can pass it to our architect to compile our hardened setup installer.
