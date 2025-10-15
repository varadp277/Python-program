with open('file1.bin', 'wb') as file:
    file.write(b'This is binary example content.\nAnd a second binary line.')

with open('file1.bin', 'rb') as file:
    content = file.read()

with open('file2.bin', 'wb') as file:
    file.write(content)
