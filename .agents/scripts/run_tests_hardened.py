import subprocess
import time
import os

def kill_child_processes(parent_pid):
    """Recursively sweep and kill all descendant processes under Windows 10."""
    try:
        import psutil
        parent = psutil.Process(parent_pid)
        children = parent.children(recursive=True)
        for child in children:
            print(f"Force terminating descendant process PID {child.pid}...")
            child.terminate()
        psutil.wait_procs(children, timeout=5)
    except ImportError:
        # Fallback to taskkill on Windows
        print("psutil not installed, falling back to taskkill /T /F...")
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(parent_pid)], capture_output=True)
    except Exception as e:
        print(f"Process sweep warning: {e}")

print("Process Tree Sweeper Module successfully initialized!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cmd = sys.argv[1:]
        proc = None
        try:
            proc = subprocess.Popen(cmd)
            proc.wait()
            sys.exit(proc.returncode)
        finally:
            if proc:
                kill_child_processes(proc.pid)
