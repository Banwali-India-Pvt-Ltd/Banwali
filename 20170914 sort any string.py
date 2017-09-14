# Program to sort alphabetically the words form a string provided by the user

my_str = raw_input("Please enter string here:")

#my_str = input("Enter a string: ")

# It will break the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# Print sorted words here

print("The sorted words are:")
for word in words:
   print(word)