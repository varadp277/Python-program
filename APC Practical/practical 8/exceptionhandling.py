try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ValueError:
    print("Invalid input! Please enter integers only.")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

else:
    print(f"The result of {num1} divided by {num2} is {result}")

finally:
    print("Execution completed.")
