class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) < (other.x, other.y)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) <= (other.x, other.y)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) > (other.x, other.y)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) >= (other.x, other.y)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))

# クラスの使い方
point1 = Point(1, 2)
point2 = Point(1, 2)

print(point1)           # Point(1, 2)
print(point1 == point2) # True
print(point1 < point2)  # False

point_set = {point1}
print(point2 in point_set)  # True
