import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y}) ")

    def move(self, x0, y0):
        self.x = self.x + x0
        self.y = self.y + y0

    def distance(self, b):
        x2 = b.x
        y2 = b.y
        distance = math.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2)
        distance = round(distance, 3)
        print(distance)


a = Point(2, 3)
b = Point(5, 3)

a.show()
a.move(5, -5)
a.show()
a.distance(b)
