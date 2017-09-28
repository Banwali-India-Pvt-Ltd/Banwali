a=input("Enter the length for name:")
lst = [] #empty list
for i in range(0,a):
	i=raw_input()#Here user will input the number of insertaion
	lst.append(i)#Here list item add by user input
print lst
rs = " ".join(lst)#this will convert list items to string
print rs
s=raw_input("Enter string you want to find:")
print "The index of your search word is:", rs.find(s)#It will find the index of input word
print "Total", rs.count(s), "words are in the string" #It will count the input word