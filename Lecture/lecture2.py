# Sets are better for storing large amounts of unique objects/numbers because it is much faster to look through a set, 
# due to the nature of them being organized.

# Declare lists using brackets []
# Declare sets using curly braces {}

# Dictionaries are used to associate an object with an index. For example, a dictionary can be {nic21003: majors=[Comp Sci, Comm]}
# Use dictionary instead of set if you need to store information that isn't hashable

# Downside of sets and dictionaries is that there's no sense of order. It's hard to find a median value/next closest thing.
# Syntax for a dictionary is dict = {1: "one", 2:[2, 2, 2, 2]}
# You cannot have duplicate keys in a set or dictionary.

# type(variable) returns the type an object is
# isinstance(variable, type) returns the boolean for if a variable is of a specified type

# str(var) returns a variable as a string

# Module use:
x = 27
def mult(P1):
    return P1 * x

print(mult(3))
# You can import lecture2.py into another file and use this function now.
# import lecture2.py // THIS IMPORTS THE WHOLE FILE. NOT ONE FUNCTION!
# To import one function, do from FILENAME import FUNCTIONNAME - DO NOT use dot notation if you do this
# To use the function now, you'd do lecture2.mult(value)

# You can also access individual parts of a file by doing FILENAME.VARIABLE/FUNCTION
# When you import a file, everything in that file is executed. If you have any print statements, you will see them run.
# When you import a file as an alias, you have to type "import FILENAME as ALIAS"
# If you do "from MODULE import *" it imports everything AND you don't have to use the module name. NOT RECOMMENDED

# assert(variable/function w/ arguments) raises an error if the argument you pass does not equal the value you set it to. 
# Example:
assert mult(6) == 162
# If the function does not return 162, it raises an error. This is useful for making test cases.

# __name__ returns the current name of the file. You will always have access to this. In the file you run, it is __main__ by default.

if __name__ == "__main__": # Only runs if the file is NOT imported and is executed directly
    print("Hello!")

