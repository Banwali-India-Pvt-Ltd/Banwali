import random

# Select an even number in 100 <= number < 1000
print random.randrange(100, 1000, 2)

# Select another number in 100 <= number < 1000
print random.randrange(100, 1000, 3)

a=[1,2,3,4,5,6,7,8,9,]
print random.choice(a)#A random item from a list, tuple, or string.

print random.random() #A random float r, such that 0 is less than or equal to r and r is less than 1

lst=[1,2,3,4,5,6,7,8,9]
print random.shuffle(lst) #Randomizes the items of a list in place. Returns None.

print random.uniform(1,100) #	A random float r, such that x is less than or equal to r and r is less than y '''