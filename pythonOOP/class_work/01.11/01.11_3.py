from typing import List

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area_rect(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area_square(self):
        return self.side ** 2


def calculate_total_area(shape: list[Shape] -> float):
    total_area = 0
    for obj in shape:
        total_area += obj.calculate_area()
    return total_area


r = Rectangle(5, 6)
s = Square(10)
c = Circle(1)
rects = [r, s, c]
print(calculate_total_area(rects))