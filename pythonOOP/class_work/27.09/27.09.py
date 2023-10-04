# 1 task                    Беспятий Дмитро
# import math
# class Point:
#     """Class Point2D"""
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __eq__(self, other): # порівняння значень
#         if self.x == other.x and self.y == other.y:
#             return True
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Point): # перевірка обьекта чи е він екземпляром Поинт
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Point(new_x, new_y) # повернення нової точки з новим обьектом
#         elif isinstance(other, (int, float)):
#             new_x = self.x + other
#             new_y = self.y + other
#             return Point(new_x, new_y)
#         else:
#             raise TypeError("Невірний тип операнда")
#
#     def __radd__(self, other): # 5 + A:  self = A, other = 5
#         return self.__add__(other)
#         # new_x = self.x + other
#         # new_y = self.y + other
#         # return Point(new_x, new_y)
#
#     def __len__(self):
#         return abs(self.x) + abs(self.y)
# #
# # if __name__ == "__name__"
# # A = Point(-1,3)
# # B = Point(2,3)
# # print(A)
# # print(B)
# # print(id(A), id(B))
# # print(A == B)
# # A == B  # self = A, other = B
# # C = 5 + A
# # print(C)
# # print(f"len A = {len(A)}")
#
# # 2 task                    Беспятий Дмитро
#
# class Circle:
#
#     """Class Circle"""
#
#     def __init__(self, radius, x=0, y=0):
#         self.radius = radius
#         self.point = Point(x, y)
#
#     def __repr__(self):
#         return f"Circle r={self.radius} with point {self.point}"
#
#     def __eq__(self, other): # метод порівняння
#         return self.radius == other.radius
#
#     # def __ne__(self, other):
#     #     return not self.__eq__(other)
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __iadd__(self, other):
#         # return Circle(self.radius + other, self.point.x, self.point.y)
#         self.radius += other
#         return self
#
#     def __len__(self):
#         return self.__int__()
#
#     def __int__(self):
#         l = 2 * math.pi * self.radius
#         return math.trunc(l)
#
#     def __float__(self):
#         return 2 * math.pi * self.radius
#
#
# c1 = Circle(1, 0, 0)
# c2 = Circle(2, 1, 1)
# print(len(c1))
# print(int(c1))
# print(float(c1))
# print(c1)
# print(c2)
# print(c1 == c2)
# print(c1 >= c2)
# print(c1 < c2)
# print(c1, id(c1))
# c1 += 5
# print(c1, id(c1))


# 3 task                    Беспятий Дмитро

class Student:

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __str__(self):
        return f'Repr: {self.name} - {self.scores}'

    def __repr__(self):
        return f'Str: {self.name} - {self.scores}'

    def __getitem__(self, index):# повертає індекс
        return self.scores[index]

    def __setitem__(self, index, value):
        self.scores[index] = value

    def __delitem__(self, index):
        print(f"Виконується видалення по індексу {index}")
        del self.scores[index]

    def __call__(self, semester):
        print(f"Виклик на сесію {semester}")

    # def __getattr__(self, item):  # перевірка чи є заданий ітем в класі
    #     print("get attribute")

    def __getattribute__(self, item):
        print("get attribute name")
        if item == 'name':
            return 5

A = Student("Alice", [5, 6, 8, 12])
print(A.name)

# print(A.scores[-1])
# print(A[0])
# print(*A)
# A[0] = 12
# print(A)
# del A[0]
# print(A)
# A("III")
#
# for score in A.scores:
#     print(score)





