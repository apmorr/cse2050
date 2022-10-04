# Test-driven development
# Three phrases:
# 1) Red, 2) Green, 3) Refactor

# Red phrase: Write a test and make sure that it fails. 
# Assertion statements should be written and ran before you begin writing functions. Make sure it fails for expected reason.
# Write skeleton code (define function with pass as body to begin writing)

# Green phrase: Code works as intended after running all debugging.

# Refactor phase: Find ways to get rid of repeated functionality.


# Object-oriented Programming (OOP)
# Programming foucsed around objects
# x = []
# x is an instance of a list (class).

# encapsulation is assigning multiple attributes to an object.
# example of creating an object: c1 = Car(max_speed = 50, make = "Toyota")
# c2 = Car(max_speed = 60, make = "Dodge")

# Making a new class!
# __init__ is a reserved keyword

import math

class Vector():
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2
    
    def magnitude(self):
        return (self.x**2 + self.y**2) ** (1/2)

class PolarVector(Vector): # Subclass of Vector, has all Vector attributes plus some special ones. Inheritance
    def angle(self):
        return math.atan(self.y/self.x)

v1 = Vector(3, 4) # calls Vector.__init__() with v1
v2 = Vector(4, 5)

assert v1.x == 3
assert v1.y == 4

p1 = PolarVector(2, 2)

print(Vector.magnitude(v1))
assert v1.magnitude() == 5
assert p1.angle() == 45




# Inheritance

# A way of making a class that is a subclass
# Object class has children integer, string, list, custom made classes, etc.

