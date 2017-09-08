#simple calculator for simple mathmatical calculation
num1 = int(input("Please enter any number for calculate:"))#user's first choice for calculation
num2 = int(input("Please enter another number for calculate:"))#user's second choice for calculation
operation = raw_input('Please enter sign for calculation:')#user's operation input box for calculating

if operation ==  '-': #code block for calculation
    print (num1 - num2)
elif operation == '+':
    print (num1 + num2)
elif operation == '/':
    print (num1 / num2)
elif operation == '*':
    print (num1 * num2)
elif operation == '%':
    print (num1 % num2)
else:
    print ("You entered wrong operend for calculation")