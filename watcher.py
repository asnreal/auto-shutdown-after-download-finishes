import os
import time
import subprocess

# Ask for path until valid
while True:
    path = input("Enter the folder path to watch: ").strip()
    if os.path.exists(path) and os.path.isdir(path):
        break
    else:
        print("Invalid folder path. Try again.")

check_interval = 25
stable_checks_needed = 3
shutdown_delay = 60

def get_folder_size(folder):
    total = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
            except:
                continue
    return total

print(f"Watching folder: {path}")
print(f"PC will shut down automatically after {check_interval*stable_checks_needed} seconds of idle.")

last_size = get_folder_size(path)
stable_counter = 0

try:
    while True:
        time.sleep(check_interval)
        try:
            current_size = get_folder_size(path)
        except:
            continue

        if current_size != last_size:
            last_size = current_size
            stable_counter = 0
            print("Download active...")
        else:
            stable_counter += 1
            if stable_counter >= stable_checks_needed:
                print(f"Folder stable. Shutting down in {shutdown_delay} seconds...")
                subprocess.run(["shutdown", "/s", "/t", str(shutdown_delay)])
                break
except KeyboardInterrupt:
    print("Script stopped by user.")
