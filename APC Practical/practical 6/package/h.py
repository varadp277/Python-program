# create an directory 

import os

new_folder = r'D:\DYP Course\Third Year\APC Practical\practical 7\package\new_folder'
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"Directory created: {new_folder}")
else:
    print(f"Directory already exists: {new_folder}")
