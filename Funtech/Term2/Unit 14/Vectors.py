class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

"""
square = [Vector(0, 0),
          Vector(100, 0),
          Vector(0, 100),
          Vector(100, 100)]

for point in square:
    print(point)

"""
v1 = Vector(100, 0)
v2 = Vector(0, 100)
print(v1 + v2)

# i5-9400F
# 16GB RAM
# 1TB HDD
# GTX 1660
