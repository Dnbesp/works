# task 1                                    Беспятий Дмитро
# class Book:
#
#     """Методи __detattr__(), __setattr__(), __getattribute__(), __delattr__()"""
#
#     def __init__(self, title, author):
#         self._attributes = {"title": title, "author": author}
#
#     # 3. Імплементуйте метод `__getattr__`, щоб реалізувати динамічне отримання відсутніх атрибутів.
#     # Коли об'єкт намагається отримати відсутній атрибут, то повертати значення відповідного атрибута із словника
#     # _attributes через ключ. Якщо ж відповідного атрибута нема і у словнику, то викликати виключення AttributeError.
#     def __getattr__(self, name):
#         print(f"Call __getattr__{name}")
#         if name in self._attributes:
#             return self._attributes[name]
#         else:
#             raise AttributeError(f"'Book' object has no attribute '{name}'")
#
#     # 4. Доімплементуйте метод `__setattr__()`, що дозволить нам змінювати атрибути об'єкта при присвоєнні значення.
#     def __setattr__(self, name, value):
#         print(f"Call __setattr__with {name=} {value=}")
#         if name == "_attributes":
#             super().__setattr__(name, value)
#         else:
#             self._attributes[name] = value
#
#     # 5. Визначте метод __delattr__(self, name), щоб видаляти атрибут name об'єкта із словника _attributes при
#     # використанні ключового слова `del`. Якщо у словнику такого атрибуту із іменем namе нема, то викличіть виняток
#     # AttributeError.
#     def __delattr__(self, name):
#         del self._attributes[name]
#
#     # 6. Імплементуйте метод `__getattribute__()`, коли об'єкт намагається отримати будь-який атрибут.
#     def __getattribute__(self, name):
#         print(f"Call __getattribute__ with {name=} ")
#         if name in ("_attributes", '__dict__'):
#             super().__getattribute__(name)
#             return super().__getattribute__(name)
#         else:
#             raise AttributeError(f"'Book' object has no attribute '{name}'")

# 1,2
# book = Book("Python Programming", "John Zelle")
# print(book.__dict__)
# print(book.title, book.author)
# print("3----------")
# # 3
# print("book.title=", book.title)
# print("book.author=", book.author)
# # print("book.year=", book.year)
# print("4----------")
# # 4
# book.year = 2016
# print(book.__dict__)
# print("book.year=", book.year)
# print("5----------")
# # 5
# del book.author
# print(book.__dict__)
# print("6----------------------------------------")
# # 6
# book.year = 2016
# print("6.1----------------------------------------")
# print(book.__dict__)
# print("6.2----------------------------------------")
# print("book.year=", book.year)


# task 2                                    Беспятий Дмитро

class Dynamic:

    """class Dynamic - methods(__getattr__, __setattr__, __delattr__, __getattribute__)"""

    _attributes = {}

    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name):
        print(f"Call __getattr__{name}")
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"'Book' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        print(f"Call __setattr__with {name=} {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value

    def __delattr__(self, name):
        print(f"del -> {name}")
        del self._attributes[name]

    def __getattribute__(self, name):
        print(f"Call __getattribute__ with {name=} ")
        if name == 'old':
            raise AttributeError(f"'old' protected attribute '{name}'")
        return super().__getattribute__(name)

d = Dynamic()
print("---------------")
d.name = 'Dima'
d.old = 35
d.day = "to day is thursday"
print(d.__dict__)
print("---------------")
print(d.name)
print("---------------")
del d.day
print(d.__dict__)
print(Dynamic().__dict__)
print("---------------")
print(d.old)













