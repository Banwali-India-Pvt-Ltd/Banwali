
lst = ['Java', 'Jython', 'Groovy', 'Scala', 'Jruby']

# How many JVM langs do you know ?
print 'I know of ', lst.__len__(), 'langs that can run on the JVM'

# It's not a good idea to directly us __xxx__ methods
# A better way is. Remember there is usually a top level function which
# is the idoimatic way to access the __xxx__method
print 'I know of ', len(lst), 'langs that can run on the JVM'

print 'Oops I forgot Clojure'
lst.append('Clojure')

# Let's iterate across the list
for lang in lst:
    print lang

# Can we get the 3rd element of the list ?
print "The 3rd JVM language is ", lst[2]
print "The first 3 JVM languages are ", lst[:3]
print "The 2nd to 4th JVM languages are ", lst[1:4]

print "let's sort these languages"
lst.sort()
print lst
