class Point:
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_size(self):
        return self.x * self.y

p = Point(3, 4)
print(p.get_size())
print(p.x)


class PointB(Point):
    def __init__(self, name):
        self.name = name
        Point.__init__(self)

p2 = PointB(3, 3, "Bob")
print(p2.color)
