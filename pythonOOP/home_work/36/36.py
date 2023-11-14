# task 1        Беспятий Дмитро

# def decorator(fn):
#     def wrapper(a, b):
#         if type(a) == float and type(b) == float and b != 0:
#             return fn(a, b)
#     return wrapper
#
# @decorator
# def divide(a: float, b: float) -> float:
#     print('виконується ділення')
#     return round(a / b, 2)
#
# print(divide(4.9, 2.3))

# task 2        Беспятий Дмитро

# def check(count, price):
#     print(f"check=|{count}|{price}|")
#     summa = count * price
#     return f"{summa} UAH"
#
# print(check(2, 10))
# print()

# A
# def decorator(func):
#     def decor_check(count, price):
#         summa = func(count, price).split()[0]
#         result = f'{round(float(summa)/ 37.8, 2)} USD'
#         return result
#     return decor_check
#
# @decorator
# def check(count, price):
#     print(f"check=|{count}|{price}|")
#     summa = count * price
#     return f"{summa} UAH"
#
# print(check(2, 10))
# print()

# B
# def create_decorator(rate):
#     def decorator(func):
#         def decor_check(count, price):
#             summa = func(count, price).split()[0]
#             result = f'{round(float(summa) / rate, 2)} USD'
#             return result
#         return decor_check
#     return decorator
#
# @create_decorator(rate=40)
# def check(count, price):
#     print(f"check=|{count}|{price}|")
#     summa = count * price
#     return f"{summa} UAH"
#
# print(check(2, 10))
# print()

# task 3        Беспятий Дмитро

# from time import time
#
# def timer(fn):
#     def f1():
#         stat = time()
#         fn()
#         end = time()
#         delta_time = end - stat
#         return f'Time work fn = {delta_time}'
#     return f1
#
#
# @timer
# def fn():
#     res = ''
#     for i in range(10 ** 6):
#         res += ' '
# print(fn())
#
#
# @timer
# def fn():
#     res = ' ' * 10**6
# print(fn())

# task 4        Беспятий Дмитро

# 1, 2
from time import time, sleep


def timer(fun):
    def event(a, b):
        start = time()
        lst = []
        for num in range(a, b + 1):
            if num % 2 == 0:
                sleep(1)
                lst.append(num)
        stop = time()
        print(round((stop - start), 3))
        return fun(a, b)
    return event


def log(fun):
    def event(a, b):
        print('{} a={} b={}'.format(fun.__name__, a, b))
        return fun(a, b)
    return event


@timer
@log
def even_nums(a, b):
    lst = []
    for num in range(a, b+1):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(even_nums(2, 10))



