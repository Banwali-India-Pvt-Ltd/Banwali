# Grade calculation program for the entered marks
name = raw_input("Please enter your name:")
while name == "":
    name = raw_input("Please enter your name:")
if name == name:

    marks_computer = int(input("Please enter your computer subject marks:"))
    marks_math = int(input("Please enter your math subject marks:"))
    marks_spanish = int(input("Please enter your spanish subject marks:"))

if (marks_math < 33) or (marks_spanish < 33) or marks_computer <33:
    print "Fail"
else:
    print "pass"
total = (marks_computer+marks_math+marks_spanish)
print "Your total marks are:", total,
percentage = float(total/3)
print "Your percentage are:", percentage,"%"
if percentage >75:
    print 'Your grade is Detection'
elif percentage <75 and percentage > 60:
    print "Your grade is First"
elif percentage < 60 and percentage > 50:
    print "Your grade is Second"
elif percentage <50 and percentage > 40:
    print "Your greade is Third"
else:
    print "Fail! You are not eligable for next class"

print ("name\t" "Marks in computer\t" "Marks in math\t" "Marks in spanish\t" "Result")
print name,"\t""\t""  \t", marks_computer, "  \t""\t""\t" " \t", marks_math, "\t""\t""\t""   \t", marks_spanish, "\t""\t""\t",
