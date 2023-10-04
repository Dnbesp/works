# 1  task                       Беспятий Дмитро

# import math
#
# class Circle:
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def __str__(self):
#         return f'radius circle = {self.radius}'
#
#     # Визначення площі круга
#     def sq_circle(self):
#         sq = math.pi * self.radius ** 2
#         return round(sq, 2)
#
#     # Визначення довжини кола
#     def leng_circle(self):
#         leng = math.pi * self.radius * 2
#         return round(leng, 2)
#
# fig = Circle(2)
# fig2 = Circle(3)
# print(fig)
# print(fig2)
# print(f'square circle 1 = {fig.sq_circle()}')
# print(f'length circle 2 = {fig2.leng_circle()}')


# 2  task                       Беспятий Дмитро

class Car:
    model_car = ''
    release_year = ''
    producer = ''
    engine_capacity = ''
    car_color = ''
    price = ''
    total = 0

    def __init__(self, model_car, release_year, producer, engine_capacity, car_color, price):
        self.model_car = model_car
        self.release_year = release_year
        self.producer = producer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price
        Car.total += 1

    def __str__(self):
        return f"Назва моделі: {self.model_car}, Рік випуску: {self.release_year}, Виробник: {self.producer}, " \
               f"Об'єм двигуна: {self.engine_capacity}, Колір авто: {self.car_color}, Ціна: {self.price}"

    # зміна кольору автомобіля
    def color_car(self, color):
        self.car_color = color

    # зміна ціни на автомобіль
    def price_car(self, price):
        self.price = price

    # загальна кількість автомобілів
    def total_car(self):
        return Car.total


car_1 = Car('Skoda', 2007, 'Czech Republic', 1.6, 'Grey', 6500)
print(car_1)
car_2 = Car('Toyota', 2023, 'Japan', 2.5, 'Grey', 47000)
print(car_2)
car_1.color_car('Black')
print(car_1)
car_2.price_car(45000)
print(car_2)
print(f'Загальна кількість автомобілів: {car_1.total_car()}')


