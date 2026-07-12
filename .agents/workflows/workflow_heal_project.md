# Autonomic Self-Healing Workflow (`/workflow-heal-project`)

This workflow guides the Antigravity 2.0 agent through the complete MAPE-K sensation, isolation, remediation, and self-evolution sequence on Windows 10. It utilizes `run_tests_hardened.py` to prevent Windows process file locking during compilation and testing.

## Step 1: Read the Active Anomaly State (Monitor & Sensation)
The agent must read the cached anomaly payload to understand the exact failure.
*   **Action**: Inspect the persistent cache under the system-allocated app data directory (exposed via the `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%` environment variable).
*   **State File**: `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%\healing-state.json`
*   **Instruction**: Parse the `errorDetails` and `activeAnomaly` properties. Do not look in `.agents/scratch/` since Strict Mode blocks ignored paths.

## Step 2: Classify the Failure (Analyze)
Activate the `@heal-and-evolve` skill to categorize the issue.
*   **Action**: Evaluate the error string against the taxonomy defined in `.agents\rules\development-ontology.md` (e.g., `ToolFailure`, `InputCorruption`).
*   **Instruction**: Select the correct validation command (e.g., compile vs unit test check) needed to prove the bug is resolved.

## Step 3: Spin Up Isolated Workspace (Execute - Isolation)
To safeguard the local working directory from concurrent writes and file locks, delegate the fix to an isolated workspace.
*   **Action**: Call `invoke_subagent` and explicitly choose **New Worktree Mode**.
*   **Boundary Checklist**:
    *   Verify the directory has an underlying `.git` initialization.
    *   Confirm the subagent starts on a clean slate context with no token bloat.

## Step 4: Remediate and Validate with Hardened Execution (Execute - Remediation)
Inside the temporary Git worktree, apply the code modifications and validate the fix.
*   **Action**: Execute the test or compilation step using our hardened process-tree runner. This prevents lingering background background daemons or compile-watchers from holding Windows file handles.
*   **Execution Template**:
    ```cmd
    python run_tests_hardened.py <your-test-or-compile-command>
    ```
    *Example*: `python run_tests_hardened.py pytest` or `python run_tests_hardened.py npm test`
*   **Validation Rule**: The repair is only successful when the hardened process wrapper returns a clean `exit 0` status.

## Step 5: Clean Up and Merge (Execute - Resolution)
*   **Action**: Once tests return 100% green, commit the changes inside the worktree and merge them back to the active local branch.
*   **Instruction**: Signal completion to the parent agent. This terminates the subagent and automatically wipes the temporary Git worktree from your host disk (which succeeds flawlessly because `run_tests_hardened.py` terminated all locking file handles).

## Step 6: Harden and Compact Project Knowledge (Knowledge & Self-Evolution)
Prevent the same defect from re-occurring by codifying the lesson.
*   **Action**: Write or update a dedicated rule under `.agents\rules\<defect-class>.md`.
*   **Character Cap Gate**: Ensure the rule file remains well under the hard **12,000-character platform limit** [7].
*   **Policy**: Implement a rewrite-in-place compacting strategy. Never append raw stack traces or logs to rule files; refer to `/workflow-evolve-rules` to compact if approaching the limit [8].
*   **State Reset**: Reset the state in `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%\healing-state.json` by updating `"status"` to `"resolved"`.

