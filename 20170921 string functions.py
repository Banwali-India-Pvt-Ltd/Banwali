#String functions examples
a = 'fog chal raha hai' #Variable for hold the string value
b = list(a) #This function converts string to a list
print b
print a.istitle() #This function checks that first word is title or not
print a.title()#This function converts first word of string lower to capital
print a.count('a')# This function counts a specific word in a string
print a.capitalize()# This function converts all the strings in capital form
print a.center(50,'*')# This method returns centered in a string of length width.
print a.endswith("chal")#this function chek that string end with specific word or not
print a.islower()#This function checks lower word of a string
print a.lower()#This function converts all srtings in lower form
print a.upper()#This function converts all strings in upper form
print a.find('a')#This function find and diplay position of specific word in a string
print a.isalnum()#This method checks whether the string consists of alphanumeric characters.
print a.isalpha()#This method returns True if all characters in the string are alphabets. If not, it returns False.
print a.isspace()#This method checks whether the string consists of whitespace..
print a[: :-1] #This is string slicing and it prints stirng in reverse form..