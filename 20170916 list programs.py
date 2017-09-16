list = []
list.append(1)
list.append(2)
list.append(6)
list.append(3)

print(list)

list = ["Orange", "Apple"]

# Insert at index 1.
list.insert(1, "tomato")

print(list)

# Two lists.
a = [1, 2, 3]
b = [4, 5, 6]

# Add all elements in list "b" to list "a."
a.extend(b)

# List "a" now contains six elements.
print(a)

animals = []
animals.append("cat")
animals.append("dog")
count = len(animals)

# Display the list and the length.
print(animals)
print(count)

Output

['cat', 'dog']
2