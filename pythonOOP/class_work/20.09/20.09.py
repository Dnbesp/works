class Person:

    def __init__(self, name, age=0):
        print("Begin")
        self._name = name
        self.__age = age

    def __str__(self):
        return f'{self._name} {self.__age}'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        try:
            if age < 0:
                raise ValueError('Age is not positive')
            self.__age = age
        except ValueError:
            print('Value is not changed')



obj = Person("Jon", 20)
print(obj)
# obj.set_age(10)
print(obj)
print(obj.age)
obj.age = -5
print(obj.age)
print(obj)


# class Person(object):
#
#     def __new__(cls, name, age):
#         print('Begin magic method')
#         return super().__new__(cls) # super()=object
#
#     def __init__(self, name, age=0):
#         print("Begin")
#         self.x = name
#         self.age = age
#
#     @classmethod
#     def make(cls, name, year):
#         print(f'Before create odj: {name} {year}')
#         return cls(name, 2023 - year)
#
# obj = Person("Jon", 20)
# print(vars(obj))


# class MyClass:
#     rate = '123'
#
#     def __init__(self, x, age=0):
#         print("Begin")
#         self.x = x
#         self.age = age
#
#     @staticmethod
#     def get_type(n):
#         result = MyClass.rate * n
#         print(result)
#
#     def get_type_2(self, n):
#         result = type(self).rate * n
#         print(result)
#
#     @classmethod
#     def get_type_3(cls, n):
#         result = cls.rate * n
#         print(result)
#
#     @classmethod
#     def make(cls, n, year):
#         print(f'Before create odj: {n} {year}')
#         cls.new_attr = 'attr_class' # атребут класу
#         age = 2023 - year
#         new_obj = cls(n, age)
#         return new_obj
#
#
# same_obj = MyClass.make(10, 2000)
# print(same_obj.__dict__)


# obj = MyClass(5)
# MyClass.get_type_3(10) # get_type_3(MyClass, n)
# obj.get_type_3(10) # using only cls


# obj = MyClass(5)
# MyClass.get_type(3)
# obj.get_type(3)
# print(type(obj))
# print(MyClass.__dict__)
# print(MyClass.__name__)
# print(MyClass.__module__)
# obj.__dict__['color'] = 'black'
# obj.color = 'black'
# print(obj.__dict__)
# print(obj.color)
# print(hasattr(obj, 'color'))
# setattr(obj, 'age', 3)
# print(hasattr(obj, 'age'))
# delattr(obj, 'age')
# print(hasattr(obj, 'age'))




