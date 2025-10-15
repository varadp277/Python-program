# Efficient directory iterator

import os

path = r'D:\DYP Course\Third Year\APC Practical\practical 7\package'
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_dir():
            print(f"Directory: {entry.name}")
        else:
            print(f"File: {entry.name}")
