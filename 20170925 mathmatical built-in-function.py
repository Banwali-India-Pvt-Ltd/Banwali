#Here some example about built-in function of python
import math
x= 48.25
print "The factorial of number", x, "is =", math.factorial(5)#abs(x)#The absolute value of x: the (positive) distance between x and zero.

square = 16
print "The square of number",square, "is =", int(math.sqrt(square))#SQER retruns square root of a given number

print math.ceil(x)#The ceiling of x: the smallest integer not less than x

x1,y1 = 50,40

print cmp(x1, y1) #-1 if x1 < y1, 0 if x1 == y1, or 1 if x1 > y1

print math.exp(x) #The exponential of x: ex

a1= -85.50
print float(math.fabs(a1))#The absolute value of number.

b1=41.44
print math.floor(b1)#The floor of x: the largest integer not greater than x

log = 5
print math.log(log)#The natural logarithm of x, for x> 0

print math.log10(log) #The base-10 logarithm of x for x> 0 .

print "The large number between", x1, "and", y1, "is =", max(x1,y1)#The largest of its arguments: the value closest to positive infinity

print "The small number between", x1, "and", y1, "is =",min(x1, y1)#The smallest of its arguments: the value closest to negative infinity

print math.modf(x1)# The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float

pow1 = 5
pow2 = 4
print math.pow(pow1,pow2) #The value of x**y.

