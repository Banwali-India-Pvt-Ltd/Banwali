#program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included)
n=int(raw_input("Enter an integer number:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print d