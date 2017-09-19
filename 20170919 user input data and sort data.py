s=[]
while True:
    s = raw_input("Enter strings:")
    if s:
        words = [word for word in s.split(" ")]
    else:
        break;
print " ".join(sorted(list(set(words))))