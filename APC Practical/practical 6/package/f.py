# Recursive directory traversal

import os

path = r'D:\DYP Course\Third Year\APC Practical\practical 7\package'
for root, dirs, files in os.walk(path):
    print("Current directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)
    break  # Remove break to go through entire tree
