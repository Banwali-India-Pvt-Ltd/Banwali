dict1 = {'name' : "Raj", 'age': 30, 'Course': 'Python', 'Address' : 'Mindkiya'}
dict2 = {'name' : "Kuldeep", 'age': 20, 'Course': 'Java', 'Address' : 'Banwali'}
stock = {'Banana' : 5, 'Apple': 4, 'Pears': 7,'Grapes': 8}
price = {'Banana' : 10, 'Apple': 15, 'Pears': 25,'Grapes': 24}

print cmp(dict1, price)

#Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
print len(dict2)

#Produces a printable string representation of a dictionary
print str(dict1)

#Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
print type(dict1)

#Removes all elements of dictionary dict
print dict1.clear()
print dict1


#Returns a shallow copy of dictionary dict
dict1=dict2.copy()
print dict1

#Returns a list of dict's (key, value) tuple pairs
print price.items()


#Returns list of dictionary dict's keys
print stock.keys()
print stock.values()
print stock.viewitems()

#Adds dictionary dict2's key-values pairs to dict
dict2.update(dict1)
print dict1