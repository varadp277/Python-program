# Write a PYTHON program to sum the given sequence 1+ 1/1! + 1/2! + 1/3! + ... + 1/n!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter the value of n: "))

total_sum = 0.0
for i in range(n + 1):
    total_sum += 1 / factorial(i)

print("Sum of the sequence is:", total_sum)
