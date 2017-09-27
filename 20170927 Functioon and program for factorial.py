#Function for calculate factorial of a number:
def fact(x):
    if x == 0: #This statement will get excute function
        return 1
    return x * fact(x - 1)# In this statement run till x = 0

x=int(raw_input("Enter a number to get factorial:"))
print fact(x)


#Program for calculate factorial of a given number
num=int(input("Enter a number to get factorial:"))
n=1
while num > 0:
    n = n*num
    num = num-1

print n