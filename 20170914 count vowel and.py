#Program for count vowels and consonant in a string
string=raw_input("Enter string:")#User input for string
vowels=0
for i in string: #Here by help of this loop will count vowels
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels = vowels+1
        consonant = len(string)-vowels #Here by help of len function we can get remains words of consonant
#Pring statement for values
print 'Number of total words are:', len(string)
print "Number of vowels are:", vowels
print "Number of consonant:" , consonant 