import os

# Lists all files and directories in the current directory
items = os.listdir()
print(items)

# Lists all files and directories in a specific directory
directory_path = r'D:\DYP Course\Third Year\APC Practical\practical 7'
try:
    items = os.listdir(directory_path)
    print(items)
except FileNotFoundError:
    print(f"Error: The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Error: No permission to access {directory_path}.")
