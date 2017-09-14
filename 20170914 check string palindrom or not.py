# Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = raw_input("Please enter any string:")

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print "That is a palindromic string:",my_str
else:
   print "That is not a palindrome string:",my_str