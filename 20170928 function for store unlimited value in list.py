#Python program for store value in a empty list
lines = []
while True: #This loop will continue till enter empty
    s = raw_input()
    if s:
        lines.append(s.upper())#This line will add and change values into upper case
    else:
        break #If user enter any empty calue then loop will terminate

print lines