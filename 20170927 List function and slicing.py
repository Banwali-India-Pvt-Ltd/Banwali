words = 'The quick brown fox jumps over the lazy dog'.split()
print words

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print i

print '\n'
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print S; print V; print M