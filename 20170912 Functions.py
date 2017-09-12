# Function definition is here
name = raw_input("Please enter your Name:")
age = int(input("Please enter your age:"))
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

# Now you can call printinfo function
printinfo(age=45, name="sher")
#This function is work only work on user defined function
#It will print only user defined printinfo function value
#Whatever you entered in input box it doesn't impact on printinfo function

