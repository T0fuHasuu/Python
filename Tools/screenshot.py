# Set up to sync
import sys
import subprocess
import pkg_resources

# Define required libraries
required = {'pyscreenshot'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# Install missing packages
if missing:
    print(f"Installing missing packages: {missing}")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing])

# Import required modules
import pyscreenshot as ImageGrab
from tkinter import *

# Screenshot Function 
def Shot():
    # Hide GUI
    root.withdraw()
    
    # ScreenShot the Screen
    image = ImageGrab.grab()
    
    # Reappear
    root.deiconify()
    
    # Display Screenshot
    image.show()

# Create parent window
root = Tk()

# Screenshot Button
screenshot = Button(root, text="Screenshot", command=Shot)
screenshot.pack()

# Start the GUI loop
root.mainloop()
