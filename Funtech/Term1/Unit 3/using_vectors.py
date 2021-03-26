import math


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        return Vector2D(new_x, new_y)

    def __eq__(self, other: "Vector2D") -> bool:
        same_x = self.get_x() == other.get_x()
        same_y = self.get_y() == other.get_y()
        return same_x and same_y

    def __len__(self):
        x_2 = self.get_x() ** 2
        y_2 = self.get_y() ** 2
        return int(math.sqrt(x_2 + y_2))

    def __mul__(self, other: float) -> "Vector2D":
        new_x = self.get_x() * other
        new_y = self.get_y() * other
        return Vector2D(new_x, new_y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        new_x = self.get_x() - other.get_x()
        new_y = self.get_y() - other.get_y()
        return Vector2D(new_x, new_y)

    def __truediv__(self, other: float) -> "Vector2D":
        new_x = self.get_x() / other
        new_y = self.get_y() / other
        return Vector2D(new_x, new_y)

    def __str__(self) -> str:
        return "[{}, {}]".format(self.x, self.y)


v1 = Vector2D(4, 10)
v2 = Vector2D(4, 10)
v3 = Vector2D(5, 10)
v4 = Vector2D(3, 4)
# print("[{}, {}]".format(v1.get_x(), v1.get_y()))
print(v1)

print(v3 - v1)
print(v3 + v1)
print(v1 * 2)
print(v1 / 2)

print(v1 == v2)
print(v2 == v3)

print(len(v4))