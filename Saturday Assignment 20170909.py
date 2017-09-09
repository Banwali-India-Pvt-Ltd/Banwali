# PYTHON PROGRAM TO CALCULATE THE GRADE

while True:
    name = raw_input("Enter your name: ")# Code block for enter user choice
    if name == name:
        print("Enter three subjects marks below:-")
        num1 = int(input("Math:"))
        num2 = int(input("Computer:"))
        num3 = int(input("Spanish:"))
        total = (num1+num2+num3)
        print 'your total marks are:', num1, '+' , num2, '+', num3,'=', total
        average = float(total/3)
        print 'Your percentage are:', average,'%'
        if average < 40: #code block for grading conditions
            print 'Fail'
        elif average >40 and average <50:
            print 'Third'
        elif average > 50 and average < 60:
            print 'Second'
        elif average >60 and average <75:
            print 'first'
        elif average >75:
            print 'Detection'
        else:
            print 'Pleae enter your correct name'
