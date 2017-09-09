
# Python Program - Calculate Perimeter of Triangle

while True:
    print("Enter 'x' for exit.")
    len1 = input("Enter length of first side: ")
    len2 = input("Enter length of second side: ")
    len3 = input("Enter length of third side: ")
    if len1 == 'x':
        break
    else:
        length1 = int(len1)
        length2 = int(len2)
        length3 = int(len3)
        perimeter = length1 + length2 + length3
        print "Perimeter of Triangle =", perimeter ,"\n"
