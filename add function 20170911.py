val1 = int(input("please enter value 1 to calculate add:"))
val2 = int(input("please enter value 2 to calculate add:"))
# Function definition is here
def sum( val1, val2 ):
   # Add both the parameters and return them."
   total = val1 + val2
   print "Inside the function : ", total
   return total;

# Now you can call sum function
total = sum( 34, 43 );
print "Outside the function : ", total