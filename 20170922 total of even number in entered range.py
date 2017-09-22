num = 0
a= input("Enter range strat number:")
b=input("Enter range last numebr:")
for i in range(a,b):
    if i%2 == 0:
        num = num + i
print "the total" ,a , "to" , b,  "of even number:", num
