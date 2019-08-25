print('''
This is a calculator program that can compute the area of the following shapes.
''')

while True:
    option = input("Enter C for Circle or T for Triangle: ")
    if option == "C" or option == "c":
        radius = float(input("Enter radius: "))
        area = 3.14159 * radius ** 2
        print('Area: %d' % (area))
    elif option == "T" or option == "t":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area: %d" % (area))
    else:
        print("invalid shape!")
        break


print("Exiting...")