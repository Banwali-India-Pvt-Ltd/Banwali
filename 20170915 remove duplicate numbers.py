# Your list with duplicate values
duplicates = [1, 2, 3, 1, 2, 5, 6, 7, 6, 8, 6]

# Print the unique `duplicates` list
print(list(set(duplicates)))

# A list with small numbers
smallNumbers = [1, 2, 3]

# Print the unique `duplicates` list without the small numbers
list(set(duplicates) - set(smallNumbers))