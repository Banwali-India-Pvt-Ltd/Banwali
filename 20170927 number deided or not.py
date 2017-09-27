l=[]
l1=[]
for i in range(1, 100):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))
for j in range(1,100):
    if j%7==0 and j%5==0:
        l1.append(str(j))





print ','.join(l)
print ','.join(l1)