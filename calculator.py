print("====================")
print("Area Calculator")
print("====================")

# list the shapes available 
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

# ask the user for a shape
shape = (int(input("Which shape: ")))

if shape == 1:                       # if it is a triangle
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = (height * base) / 2
    print("The area is ", area)
elif shape == 2:                    # if it is a rectangle
    length = int(input("Length: "))
    width = int(input("Width: "))
    area = (length * width)
    print("The area is ", area)
elif shape == 3:                   # if it is a square
    side = int(input("Side: "))
    area = side * side
    print("The area is ", area)
elif shape == 4:                   # if it is a circle
    pi = 3.14
    radius = int(input("Radius: "))
    area = pi * (radius * radius)
    print("The area is ", area)
elif shape == 5:                  # user quits
    print("Bye!")
    exit()
else: 
    print("An error occured. Try again.")


