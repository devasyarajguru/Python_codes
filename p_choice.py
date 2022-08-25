print("Press 1 for square")
print("Press 2 for cube")

option = int(input("Enter Choice=> "))

if option==1:
    x = int(input("Enter your number==> "))
    print("Square of your number is:",x*x)

elif option==2:
    y = int(input("Enter your number==> "))
    print("Cube of your number is ", y*y*y)
    
else:
    print("Invalid Choice")
