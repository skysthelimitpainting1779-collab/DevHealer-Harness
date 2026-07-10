#!/usr/bin/env python
"""
run_tests_hardened.py
======================
A production-hardened test and compilation runner wrapper for Windows 10.
Designed to prevent Windows file-locking issues ("Access is denied") during 
automatic Git worktree deletions in Google Antigravity 2.0.

This script executes your build or test commands, monitors them, and guarantees
that all spawned child processes are recursively terminated upon completion, 
failure, or timeout. This ensures all file handles are completely released.
"""

import os
import sys
import subprocess
import time

# Attempt to import psutil for robust process tree tracking
try:
    import psutil
except ImportError:
    # If psutil is not installed globally yet, attempt to install or log warning
    psutil = None

def log_to_stderr(message):
    """
    Redirects internal logging to stderr to maintain absolute stdout hygiene,
    preventing malformed JSON parser stalls if this runner is executed inside a hook.
    """
    sys.stderr.write(f"[HARDENED-RUNNER] {message}\n")
    sys.stderr.flush()

def kill_child_processes(parent_pid):
    """
    Recursively locates and terminates all child processes spawned by the parent PID.
    Releases locked file handles on Windows 10.
    """
    if not psutil:
        log_to_stderr("WARNING: 'psutil' is not installed. Unable to recursively clean up child process trees.")
        log_to_stderr("Please run: pip install psutil")
        return

    try:
        parent = psutil.Process(parent_pid)
        children = parent.children(recursive=True)
        if not children:
            return

        log_to_stderr(f"Found {len(children)} active child process(es). Initiating cleanup...")
        
        # Phase 1: Soft terminate child processes
        for child in children:
            try:
                log_to_stderr(f"Terminating child PID {child.pid} ({child.name()})")
                child.terminate()
            except psutil.NoSuchProcess:
                pass

        # Wait briefly for processes to shut down gracefully
        gone, alive = psutil.wait_procs(children, timeout=3)
        
        # Phase 2: Force kill any stubborn survivors
        if alive:
            log_to_stderr(f"{len(alive)} processes survived termination. Initiating force kill...")
            for survivor in alive:
                try:
                    log_to_stderr(f"Force-killing PID {survivor.pid} ({survivor.name()})")
                    survivor.kill()
                except psutil.NoSuchProcess:
                    pass
                    
        log_to_stderr("All child processes successfully cleaned up.")
    except Exception as e:
        log_to_stderr(f"Error during process tree cleanup: {e}")

def run_command(command_list, cwd=None, timeout=60):
    """
    Runs the targeted development command under strict process monitoring.
    """
    my_pid = os.getpid()
    log_to_stderr(f"Starting execution of command: {' '.join(command_list)} (Parent PID: {my_pid})")
    
    start_time = time.time()
    process = None
    
    try:
        # Use shell=True for Windows command compatibility, but manage securely
        process = subprocess.Popen(
            command_list,
            cwd=cwd,
            stdout=sys.stdout,
            stderr=sys.stderr,
            shell=True
        )
        
        # Monitor the process execution
        while process.poll() is None:
            time.sleep(0.5)
            # Enforce execution timeout limits
            if time.time() - start_time > timeout:
                log_to_stderr(f"Command execution exceeded timeout of {timeout} seconds. Triggering abort...")
                process.terminate()
                break
                
        exit_code = process.returncode if process.poll() is not None else -1
        log_to_stderr(f"Command completed with exit code: {exit_code}")
        return exit_code

    except Exception as e:
        log_to_stderr(f"Execution failed with error: {e}")
        return 1

    finally:
        # ABSOLUTE SAFETY GATE: Guarantee all subprocesses and children are terminated
        log_to_stderr("Entering absolute process tree cleanup phase...")
        kill_child_processes(my_pid)

if __name__ == "__main__":
    # If no arguments are provided, output usage details
    if len(sys.argv) < 2:
        log_to_stderr("Usage: python run_tests_hardened.py <command_to_run>")
        log_to_stderr("Example: python run_tests_hardened.py npm test")
        sys.exit(1)

    # Reconstruct the command arguments
    target_command = sys.argv[1:]
    
    # Run the hardened wrapper (defaults to a 60-second timeout)
    exit_status = run_command(target_command, cwd=os.getcwd(), timeout=60)
    sys.exit(exit_status)
