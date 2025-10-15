with open('file1.txt', 'r') as file:
    content = file.read()

with open('file1.txt', 'w') as file:
    file.write('This is Data of python program .\nHere data is in a second line.')

with open('file2.txt', 'w') as file:
    file.write(content)
