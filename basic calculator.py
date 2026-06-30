#calculator

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print ("Select operation:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
p = input("Enter operation of choice (1/2/3/4): ")
if p == "1":
    print("Answer=", x+y)
elif p == "2":
    print("Answer=", x-y)
elif p == "3":
    print("Answer=", (x*y))
elif p == "4":
    if y!=0 :
        print("Answer=", (x/y))
    else:
        print ("Invalid operation")
else:
    print("Invalid input")
