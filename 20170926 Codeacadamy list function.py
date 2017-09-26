n = [1, 3, 5]
# Do your multiplication here
n[1]=n[1]*5
print n

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n

n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n

#Functioon for multiply
number = 5
def my_function(x):
    return x * 3

print my_function(number)

#Function for add values
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
    return x+y

print add_function(m, n)

#Function for concatnate string
n = "Hello"
# Your function here!
def string_function(s):
	return s + 'world'

print string_function(n)

#Function for print list index value:
def list_function(x):
  return x[1]

n = [3, 5, 7]
print list_function(n)

#Add value in list item
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)

#Function append or extend list
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n)
