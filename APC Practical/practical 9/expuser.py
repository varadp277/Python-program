class InvalidAgeException(Exception):
    pass

number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("You can drive")
except InvalidAgeException:
    print("Exception occurred: Invalid age")
