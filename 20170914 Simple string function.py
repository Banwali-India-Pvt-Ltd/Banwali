name = raw_input("Please enter any string here:")
print 'string = ', name

#first character
print 'string[0] = ', name[0]

#last character
print 'string[-1] = ', name[-1]

#slicing 2nd to 5th character
print 'string [1:5] = ', name[1:5]

#slicing 6th to 2nd last character
print 'string [5:-2] = ', name[5:-2]

#print all the string reverse
print 'string Reverse =', name[: :-1]

#print all length of string
print 'Total words in string is:', len(name)

#print all string in lower case
print 'String in lower case:', name.lower()
#pring all string in upper case
print 'String in Upper case:', name.upper()
