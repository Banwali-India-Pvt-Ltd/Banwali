lines = []
while True:
    s = raw_input("Enter a string:")
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
    print lines