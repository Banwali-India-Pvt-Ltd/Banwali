# Python Program - Calculate Area of Square

while True:
    print("Enter 'x' for exit.")
    side = input("Enter side length of Square: ")
    if side == 'x':
        break
    else:
        length = int(side)
        area_square = length * length
        print "Area of Square =", area_square, "\n"