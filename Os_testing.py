import os

# Change the current working directory
path = "C://Users//yuutd//Desktop"
os.chdir(path)

# Verify the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Display the content in the current directory
print("Content in the current directory:")
for item in os.listdir():
    print(item)

# Define the new folder name
new_folder = "T0fu"
folder_creation = os.path.join(path, new_folder)

# Check if the folder already exists
if os.path.exists(folder_creation):
    print(f"Folder '{new_folder}' already exists.")
else:
    # Create a new folder in the current directory
    os.mkdir(folder_creation)
    print(f"Created a new folder: {new_folder}")

# Change the current working directory to the new folder if it was created
if not os.path.exists(folder_creation):
    os.chdir(folder_creation)
    # Verify the current working directory after changing to the new folder
    new_current_directory = os.getcwd()
    print(f"Current working directory after changing to the new folder: {new_current_directory}")