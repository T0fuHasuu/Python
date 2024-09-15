import tkinter as tk
import json
import subprocess
import sys

def save_to_json():
    data = {
        "username": entry_username.get(),
        "password": entry_password.get(),
        "term": entry_term.get(),
        "subject_code": entry_subject_code.get(),
        "href_value": entry_href_value.get()
    }
    with open('Info.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Close the tkinter window
    root.destroy()
    
    # Run the Book_Spamming.py script
    subprocess.Popen([sys.executable, 'Book_Spamming.py'])

def run_book_spamming():
    # Close the tkinter window
    root.destroy()
    
    # Run the Book_Spamming.py script
    subprocess.Popen([sys.executable, 'Book_Spamming.py'])

# Create the main window
root = tk.Tk()
root.title("Update JSON Data")

# Set a dark theme
root.configure(bg='#1e1e1e')

# Define a custom style
style = {
    'bg': '#1e1e1e',
    'fg': '#00ff00',
    'highlightbackground': '#00ff00',
    'highlightcolor': '#00ff00'
}

# Create and place labels and entry fields
labels = ["Username", "Password", "Term", "Subject Code", "Link"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label, bg=style['bg'], fg=style['fg'], font=('Helvetica', 12)).grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(root, width=50, bg='#2e2e2e', fg='#00ff00', borderwidth=2, relief='flat', insertbackground='white')
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_username, entry_password, entry_term, entry_subject_code, entry_href_value = entries

# Create and place the save button
save_button = tk.Button(root, text="Save", command=save_to_json, bg='#00ff00', fg='#1e1e1e', font=('Helvetica', 12, 'bold'), relief='flat')
save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Create and place the run button
run_button = tk.Button(root, text="Run", command=run_book_spamming, bg='#ff0000', fg='#1e1e1e', font=('Helvetica', 12, 'bold'), relief='flat')
run_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
