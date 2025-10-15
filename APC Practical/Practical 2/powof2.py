# Write a PYTHON program that prints 1 2 4 8 16 32 ... n^2

n = int(input("Enter value of n: "))
 
limit = n**2

value =1
while value <= limit:
    print(value)
    value *=2