# use the "is" command to check if two variables point to the same value.
# ex:

x = 5
y = x
print(x is y) # returns false, because memory doesn't point to the same object despite both values being the same

g = 5
h = 5
print(g is h) # returns true, because memory points to the same chunk. 
              # this only works up to a certain number depending on Python version

print(id(g)) # id() returns unique id for specified object.
print(id(h)) # same as the ID for g

# Lists, tuples, and strings are ordered.
# Sets and dictionaries are not.

L = []
for i in range(1, 101): # Loop starts at 1, ends at 100 ("half-open range") - includes start but not the end
    L.append(i)
print(L) # Prints a list with ints 1-100

L = [i for i in range(1,101)] # Does the same thing as above, but in one line. This is called list comprehension

