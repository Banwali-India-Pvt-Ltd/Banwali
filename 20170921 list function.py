my_list1 = ['Raj', 'Amar', 'Sammandar', 'Ramesh', 'Kuldeep']
my_list2 = ['Sukhpal', 'Shivkaran', 'Uncle', 'Sandeep', 'Aladeen']
my_list3 = [2,4,6,7,8,5]
print cmp(my_list1, my_list2)#Compares elements of both lists.

#Len function
total = len(my_list2)+len(my_list1)
print 'total items of my_list1 and my_list2:', len(my_list1),'+', len(my_list2), '=', total
print 'Items in my_list1 is:', len(my_list1), '\n' 'Items in my_list2 is:',len(my_list2)# Gives the total length of the list.

#MAX function (Returns item from the list with max value)
print 'Largest value in my_list3 is:', max(my_list3)
print 'Largest value in my_list2 is:', max(my_list2)
print 'Largest value in my_list1 is:',max(my_list1)

#MIN function Returns item from the list with min value.
print 'Smallest value in my_list3 is:', min(my_list3)
print 'Smallest value in my_list2 is:', min(my_list2)
print 'Smallest value in my_list1 is:',min(my_list1)

#Appends (Add) object obj to list
my_list2.append('Dinesh')
print my_list2

#Returns count of how many times obj occurs in list
print 'The word (Raj) in my_list2 is:', my_list2.count('Raj')
print 'The word (Raj) in my_list1 is:', my_list1.count('Raj')

#(Index) Returns the lowest index in list that obj appears
print 'The index of word (Raj) in my_list1 is:', my_list1.index('Raj')

#Inserts object obj into list at offset index
my_list1.insert(3, "Sameer")
print my_list1


#[POP] Removes and returns last object or obj from list
my_list1.pop(-1)
print 'after remove the index -1 now value of my_list1 is:', my_list1

# [REMOVE] Removes object obj from list
my_list2.remove('Uncle')
print 'The value of my_list2 after removing the obj of uncle is:', my_list2


#Reverses objects of list in place
print my_list3.reverse()
print my_list2.reverse()


#This function sorts list
my_list2.sort(reverse=False)
print 'After sort assending order the my_list2 is:', my_list2
my_list2.sort(reverse=True)
print 'After sort deassending order the my_list2 is:', my_list2