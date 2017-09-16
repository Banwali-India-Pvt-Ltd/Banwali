items = ["book", "computer", "keys", "mug"]

if "computer" in items:
    print(1)

if "atlas" in items:
    # This is not reached.
    print(2)
else:
    print(3)

if "marker" not in items:
    print(4)

    list = [400, 500, 100, 2000]

    # Reversed.
    list.reverse()
    print(list)

    # Sorted.
    list.sort()
    print(list)

    # Sorted and reversed.
    list.reverse()
    print(list)


names = ["Tommy", "Bill", "Janet", "Bill", "Stacy"]

# Remove this value.
names.remove("Bill")
print(names)

# Delete all except first two elements.
del names[2:]
print(names)

# Delete all except last element.
del names[:1]
print(names)