# task 1                     Беспятий Дмитро
# class Rectangle:
#     # length = 5
#     # width = 10
#     name = 'Rectangle-area' # Змінна або атрибут класу
#
#     def __init__(self, length=1, width=1):
#         self.length = length
#         self.width = width
#
#     def __str__(self):
#         return f"Rectangle {self.length} x {self.width} = {self.area()}"
#
#     def area(self):
#         return self.length * self.width
#
#     def info(self):
#         print(f"Info: {self.length} x {self.width} = {self.area()}")
#         print("___"*10)
#
#     def change_atr(self):
#         new_length = int(input("Enter new length: "))
#         new_width = int(input("Enter new width: "))
#         self.length = new_length
#         self.width = new_width
#         print("Змінено атрибути об'єкта успішно")
#
#
# obj = Rectangle(4,5)
# obj.info()
# obj.change_atr()
# obj.info()

# print()
# obj2 = Rectangle(10)
# print(obj)
# obj2.info()


# print(obj.length, obj.width)
# print(obj.area())
# print(Rectangle.area(obj))

    # obj.length = 3
    # obj.width = 9
    # print(obj.length, obj.width)
    # # print(type(obj))
    # obj2 = Rectangle()
    # print(obj2.length, obj2.width)
    # # print(type(obj2))
    # square = obj.area()
    # print(f"{square=}")
    # print(Rectangle.length, Rectangle.width)


# task 2                     Беспятий Дмитро

# class City:
#     count = 0
#
#     def __init__(self, name, region, country, population, index):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.index = index
#         City.count += self.population
#
#     def __str__(self):
#         return f"City{self.name, self.population, self.index}"
#
#     def get_count_cities(self):
#         return City.count
#
#
# s1 = City("If", "West", "UA", 250, 76000)
# s2 = City("Kiev", "Central", "UA", 3000, 70000)
# s3 = City("Lvov", "West", "UA", 800, 75000)
#
# lst = [s1, s2, s3]
# for s in lst:
#     print(s)
#
# print(s1)
# print(s2)
# print(s3)
#
# print(f"{s1.get_count_cities()}")

# City.count = 2
# print(f"{s1.count=}")

# task 3                     Беспятий Дмитро

# class MoneyBox:
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.count = 0
#
#     def can_add(self, v):
#         if self.count + v <= self.capacity:
#             return True
#         return False
#
#     def add(self, v):
#         if self.can_add(v):
#             self.count += v
#         else:
#             print(f"Не можна добавити {v} монет")
#
# box = MoneyBox(capacity=10)
# box.add(6)
# box.add(3)
# box.add(1)
