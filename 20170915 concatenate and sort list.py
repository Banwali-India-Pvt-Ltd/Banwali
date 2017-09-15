# Concatenate `shortList` with `[4,5]`
shortList = [1,2,3]
plusList = shortList + [4,5]

#Use the `print()` method to see `plusList`
print "Total of shortList", shortList, 'and list [4,5]','=', plusList

# Use `sort()` on the `rooms` list
rooms = [1,5,3,4,2,6]
rooms.sort()

# Print out `rooms` to see the result
print 'Sorted list of list rooms is:', rooms

# Now use the `sorted()` function on the `orders` list
orders = [4,5,3,1,2,8,6,7]
new = sorted(orders)
# Print out orders
print 'Sorted list of list orders is:', new