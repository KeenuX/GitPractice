import time
import subprocess

# Your practice folder path
WATCH_DIR = r"C:\Users\keenu\OneDrive\Desktop\GitPractice"

# How often to sync (in seconds). 900 seconds = 15 minutes.
# You can change this to 1800 for 30 minutes, or 3600 for 1 hour.
SYNC_INTERVAL = 900  

print(f"Starting batch sync in {WATCH_DIR}...")
print(f"Bundling saves every {SYNC_INTERVAL // 60} minutes. Keep this open while coding!")

try:
    while True:
        # Wait for the interval duration
        time.sleep(SYNC_INTERVAL)
        
        # Check if there are any uncommitted changes
        status = subprocess.run(
            ["git", "status", "--porcelain"], 
            cwd=WATCH_DIR, 
            capture_output=True, 
            text=True
        )
        
        # If the output isn't empty, changes exist
        if status.stdout.strip():
            print("\n[*] Changes detected. Bundling and pushing...")
            
            subprocess.run(["git", "add", "."], cwd=WATCH_DIR)
            
            commit_time = time.strftime('%Y-%m-%d %H:%M')
            subprocess.run(["git", "commit", "-m", f"Practice session update: {commit_time}"], cwd=WATCH_DIR)
            
            push_result = subprocess.run(["git", "push", "origin", "main"], cwd=WATCH_DIR)
            
            if push_result.returncode == 0:
                print(f"[+] Successfully batched and synced at {commit_time}!")
            else:
                print("[-] Push failed. Will try again next cycle.")
                
except KeyboardInterrupt:
    print("\nAuto-sync stopped by user.")