#Function for get the largest number among three numbers
def largest(a,b,c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c
a = int(input("Enetr 1st Number:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))
print "The largest number is:", largest(a,b,c)
