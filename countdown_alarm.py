import tkinter as tk
import time

def countdown(t):
    # Convert time to minutes and seconds
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    
    # Update the label with the current time
    label.config(text=timer)
    
    if t > 0:
        # Call countdown function again after 1 second
        root.after(1000, countdown, t - 1)
    else:
        # Once the countdown reaches 0, display a message
        label.config(text="TIMES UP")

# Create the tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Create a label to display the countdown
label = tk.Label(root, font=('Helvetica', 48), fg='red')
label.pack(pady=20)

# Input time in seconds (this can be modified as needed)
t = int(input("Enter the time in seconds: "))

# Start the countdown
countdown(t)

# Run the tkinter event loop
root.mainloop()
