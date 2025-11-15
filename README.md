
---

# Auto Shutdown After Download Finishes

This Python script watches any folder you choose and automatically shuts down your PC once downloads or updates stop.
It’s useful for large downloads, game updates, or any situation where you want the PC to turn off automatically after files stop changing.

---

## What This Script Does

* Monitors a folder you select
* Checks if files are changing (download/update in progress)
* Detects when the folder is idle for a set time
* Triggers a Windows shutdown automatically

---

## How It Works

1. Run the script
2. Type the folder path you want to monitor
3. The script measures total file size in the folder
4. Every few seconds it checks the folder again
5. If the size keeps changing → download is active
6. If the size stays the same for several checks → download finished
7. It executes a shutdown command with a short delay

---

## Requirements

* Python 3.x
* Windows OS (shutdown command only works on Windows)
* If Windows protects the shutdown command, run the script as an **administrator**

---

## How to Run

1. Open Command Prompt or PowerShell
2. Navigate to the folder containing watcher.py, for example: cd path\to\your\script
3. Run the script: python watcher.py
4. Type the folder path to monitor, for example: C:\Program Files\Epic Games\Fortnite
5. Leave it running; your PC will shut down automatically when the folder becomes idle

**Note:** If Windows blocks the shutdown command, you must run the terminal as **Administrator**.

---

## Optional Settings

You can edit these directly in the script to adjust behavior:

* check_interval = 25 → seconds between folder size checks
* stable_checks_needed = 3 → number of consecutive stable checks to confirm folder idle
* shutdown_delay = 60 → seconds to wait before actually shutting down after idle detected

Example:

* check_interval = 10 → checks folder every 10 seconds
* stable_checks_needed = 5 → folder must be stable for 5 checks
* shutdown_delay = 30 → PC shuts down 30 seconds after idle detected

---

## Notes

* Save any open work before leaving the script running
* Shutdown delay gives you a short safety window
* Script works only while the window is open

---

## License

Free to use, modify, and share.

---
