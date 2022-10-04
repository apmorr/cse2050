# Running-time Analysis

L = ["a","b","c","d","e"] # Operations on collections (time to add an item, move an item, check membership, index an item, concatenation)
L.append("f") # ~1 operation

L.insert(0, "g") # ~6 operations (find 0 index, insert at front), move everything in list
L.pop() # ~1 operation
L.pop(0) # ~5 operations (pop item at index 0, move other elements)
