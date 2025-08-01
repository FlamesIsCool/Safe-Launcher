# SafeLauncher

🚀 A smart Roblox launcher tool that auto-suspends the your executor while launching Roblox to prevent crash, freeze, or injection conflicts. Automatically resumes the executor once Roblox is safely running.

---

## ✨ Features

- ✅ Auto-elevates to **Administrator**
- 🔧 Detects and **suspends executor** while launching Roblox
- 🚀 Cleanly **launches Roblox** without injection interference
- ♻️ Automatically **resumes executor** after Roblox launches
- 🧠 Fully Python-based & easy to modify

---

## 📂 File Structure

No extra files needed. One standalone script.

## 🛠 Requirements

- Python 3.8+
- Roblox installed (non-UWP version)
- Zenith executor must be running
- Install the `psutil` library:

```bash
pip install psutil
