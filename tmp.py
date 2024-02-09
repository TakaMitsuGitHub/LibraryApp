# class Point:
#     def __init__(self, x, y):
#         self.x: str = x
#         self.y: str = y
#
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
#
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         return False
#
#     def __lt__(self, other):
#         if isinstance(other, Point):
#             return (self.x, self.y) < (other.x, other.y)
#         return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, Point):
#             return (self.x, self.y) <= (other.x, other.y)
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Point):
#             return (self.x, self.y) > (other.x, other.y)
#         return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, Point):
#             return (self.x, self.y) >= (other.x, other.y)
#         return NotImplemented
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
# # クラスの使い方
# print("__init__")
# point1 = Point(1, 2)
# point2 = Point(1, 2)
#
# print("__repr__")
# print(point1)  # Point(1, 2)
# print(point2)  # Point(1, 2)
#
# print("__eq__")
# print(point1 == point2)  # True
# print(point1 < point2)  # False
#
# print("__hash__")
# point_set = {point1}
# print(point_set)  # {Point(1, 2)}
# print(point2 in point_set)  # True



from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


# クラスの使い方
print("__init__")
point1 = Point(1, 2)
point2 = Point(1, 2)

print("__repr__")
print(point1)  # Point(1, 2)
print(point2)  # Point(1, 2)

print("__eq__")
print(point1 == point2)  # True
# print(point1 < point2)  # エラー

print("__hash__")
point_set = {point1}
print(point_set)  # {Point(1, 2)}
print(point2 in point_set)  # True

print(point1.x)  # 1
point1.x = 3  # エラー
print(point1.x)  # 3
