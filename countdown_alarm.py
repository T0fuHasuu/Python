# Import and set as 
import tkinter as tk
import time

# Countdown Function
def countdown(t):
    # Max second with 60
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    
    # Have Timer as String
    label.config(text=timer)
    
    # Keep substract 1 till there's nothing left and wait for 3 seconds to exit
    if t > 0:
        root.after(1000, countdown, t - 1)
    else:
        label.config(text="TIMES UP")
        root.after(1500, root.destroy)  

# Widget Function
def widget():
    root = tk.Tk()
    root.title("Timer")
    
    # Static widget
    root.geometry("250x100")
    root.resizable(False, False)
    
    # Costumize color and font
    root.configure(bg='black')
    label = tk.Label(root, font=('Helvetica', 35, 'bold'), fg='white', bg='black')
    label.pack(pady=20)
    
    return root, label
    
# Process
t = int(input("Enter Seconds: "))

# recall countdown and widget function
root, label = widget()
countdown(t)

root.mainloop()

# You need tkinter install in this code