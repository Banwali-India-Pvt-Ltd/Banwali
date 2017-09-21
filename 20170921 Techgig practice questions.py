def main():
    '''finding cube root
   Enter The number '''
number=int(raw_input('Enter the number :'))
#initialize the variable to zero
root_cube=0
#using Simple While loop increment ans until cube of the 
#answer less than input
while root_cube**3<number:
    root_cube+=1
#if entered number is not perfect cube indicate that in console    
if root_cube**3!=number:
 print(str(number)+' is not perfect cube')
#if the entered number is perfect cube display the cube root  
else:

 print('cube root of '+str(number)+' is: '+str(root_cube))
main()


#Program for check area of rectangle
def main():
    length = int(input("Enter length of rectangle:"))
    breadth = int(input("Enter breadth of rectangle:"))
    area = length * breadth
    print "The area of rectangle is:", area,'sqmt'
main()


#Program for check area of a square
def main():
    length = int(input("Enter length of square:"))
    area = length * length
    print "The area of rectangle is:", area,'sqmt'
main()


#program for calculate area of triangle

def main():
    base = int(input("Enter the base of tringle:"))
    height = int(input("Enter the height of trigle:"))
    area = base * height / 2
    print area
main()