x = int(input("Enter first number of your choice:"))
y = int(input("Enter second number of your choice:"))
z = int(input("Enter third number of your choice:"))
if x>y and x>z:
    print(f"The greatest number is {x}")
elif y>x and y>z:
    print(f"The greatest number is {y}")
else:
    print(f"The greatest number is {z}")
