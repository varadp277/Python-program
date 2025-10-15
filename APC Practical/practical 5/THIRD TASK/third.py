# File Handling Example in Python

# Step 1: Write into pqr.txt
with open("pqr.txt", "w") as file:
    file.write("Hello, this is file PQR.\n")
    file.write("It contains some sample text.\n")
    file.write("We will append this into xyz.txt.\n")

print("Data written to pqr.txt successfully.")

# Step 2: Append data from pqr.txt to xyz.txt
with open("pqr.txt", "r") as source:
    data = source.read()

with open("xyz.txt", "a") as target:
    target.write(data)

print("Data from pqr.txt appended to xyz.txt.")

# Step 3: Read xyz.txt from 0th byte using seek()
with open("xyz.txt", "r") as file:
    file.seek(0)   # Move pointer to beginning
    print("\nFull content of xyz.txt:")
    print(file.read())

# Step 4: Read first 10 bytes
with open("xyz.txt", "r") as file:
    file.seek(0)
    first10 = file.read(10)
    print("\nFirst 10 bytes of xyz.txt:")
    print(first10)

# Step 5: Read first two lines using readline()
with open("xyz.txt", "r") as file:
    file.seek(0)
    print("\nFirst two lines using readline():")
    print(file.readline(), end="")  # Line 1
    print(file.readline(), end="")  # Line 2

# Step 6: Use tell() to get current position
with open("xyz.txt", "r") as file:
    file.seek(0)
    file.read(10)   # Move pointer by reading 10 bytes
    pos = file.tell()
    print(f"\nCurrent file pointer position after reading 10 bytes: {pos}")