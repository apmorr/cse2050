class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**(1/2)
    
    def __eq__(self, other):
        return (self.dist_from_origin() == other.dist_from_origin())

    def __lt__(self, other):
        return (self.dist_from_origin() < other.dist_from_origin())

    def __gt__(self, other):
        return (self.dist_from_origin() > other.dist_from_origin())

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    

if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(5, 6)
    p4 = Point(4, 3)


    assert p1.x == 3
    assert p1.y == 4

    assert p1 == p2
    assert not(p1 == p3)

    assert p1.dist_from_origin() == 5
    assert p4.dist_from_origin() == 5

    assert p1 < p3
    assert not (p3 < p1)

    assert p3 > p1
    assert not (p1 > p3)

    assert str(p1) == "Point(3, 4)"
    assert not (str(p1) == "Lol noob")