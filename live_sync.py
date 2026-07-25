import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Your practice folder path
WATCH_DIR = r"C:\Users\keenu\OneDrive\Desktop\GitPractice"

class AutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ignore changes inside the hidden .git folder to prevent infinite loops!
        if ".git" in event.src_path:
            return
            
        print(f"\n[+] Save detected: {event.src_path}")
        
        try:
            # 1. Stage all changes
            subprocess.run(["git", "add", "."], cwd=WATCH_DIR)
            
            # 2. Attempt to commit the changes
            commit_time = time.strftime('%Y-%m-%d %H:%M:%S')
            commit_cmd = ["git", "commit", "-m", f"Auto-save: {commit_time}"]
            
            # We capture the output to see if there were actually files to commit
            result = subprocess.run(commit_cmd, cwd=WATCH_DIR, capture_output=True)
            
            # 3. Push ONLY if the commit was successful (meaning new code was saved)
            if result.returncode == 0:
                print("[*] Pushing to GitHub...")
                subprocess.run(["git", "push", "origin", "main"], cwd=WATCH_DIR)
                print("[+] Successfully synced to GitHub!")
                
        except Exception as e:
            print(f"[-] Error during Git sync: {e}")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(AutoCommitHandler(), path=WATCH_DIR, recursive=True)
    observer.start()
    
    print(f"Watching for file saves in {WATCH_DIR}...")
    print("Keep this terminal open while you code. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()