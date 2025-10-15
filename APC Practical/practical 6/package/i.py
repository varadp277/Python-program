# Remove an empty directory

import os
folder_to_remove = r'D:\DYP Course\Third Year\APC Practical\practical 7\package\new_folder'
if os.path.exists(folder_to_remove):
    os.rmdir(folder_to_remove)
    print(f"Directory removed: {folder_to_remove}")
else:
    print(f"Directory does not exist: {folder_to_remove}")
