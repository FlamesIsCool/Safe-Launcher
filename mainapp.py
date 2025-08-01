import subprocess
import os
import time
import psutil
import ctypes
import sys

# === Auto-run as admin ===
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("🔐 Elevating to admin...")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{__file__}"', None, 1)
    sys.exit()

# === Paths ===
EXECUTOR_PATH = r"C:\Users\corre\Downloads\Zenith\zenith.exe"
EXECUTOR_NAME = "zenith.exe"
ROBLOX_PATH = r"C:\Users\corre\AppData\Local\Roblox\Versions\version-b8550645b8834e8a\RobloxPlayerBeta.exe"

# === Process utils ===
def find_executor_proc():
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.name().lower() == EXECUTOR_NAME and EXECUTOR_PATH.lower() in proc.exe().lower():
                return proc
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return None

def suspend_process(proc):
    try:
        proc.suspend()
        print(f"✅ Suspended: {proc.name()}")
    except Exception as e:
        print(f"❌ Failed to suspend: {e}")

def resume_process(proc):
    try:
        proc.resume()
        print(f"✅ Resumed: {proc.name()}")
    except Exception as e:
        print(f"❌ Failed to resume: {e}")

# === Launch logic ===
def launch_roblox():
    if not os.path.exists(ROBLOX_PATH):
        print("❌ RobloxPlayerBeta.exe not found.")
        return

    executor = find_executor_proc()
    if executor:
        suspend_process(executor)
    else:
        print("⚠️ Zenith not found running. Is it already open?")

    print("🚀 Launching Roblox...")
    subprocess.Popen(ROBLOX_PATH, creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(5)

    if executor:
        resume_process(executor)

launch_roblox()
