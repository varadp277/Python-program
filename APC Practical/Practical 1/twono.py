a = int(input("Enter the number of a:"))
b = int(input("Enter the number of b:"))
c = int(input("Enter the number of c:"))

if a>b & a>c:
    print("a is greater than b");
elif a<c & b<c:
    print("c is greater than a,b ");
elif b>a & b>c:
    print("b is greater than a,c");
else :
    print("Invalid value");