import random
import math
a=random.randrange(1,10)
for i in range(1,11):
    print a, 'x', i, '=', a*i

def square(a):
    return a*a

z=a
print "The square of number",z, "is", square(z)

def root_square(a):
    return a**0.5

print "The root square of number", z, "is", float(root_square(z))

def facto(a):
    return math.factorial(a)

print "The factorial(method1) of number", z, "is", facto(z)

def facto2(a):
    n = a
    num = 1
    while n > 0:
        num = n * num
        n = n - 1
    return num


print "The factorial(method2) of number", a, "is", facto2(a)