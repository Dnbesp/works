from sys import getsizeof #розмір обьекта

class User:
    __slots__ = ("username", "name", "last_name")

    def __init__(self, username, name, last_name):
        self.username = username
        self.name = name
        self.last_name = last_name

u = User("admin", "Jon", "Col")
print(type(User))
print(u.username, u.name, u.last_name)
size_u = getsizeof(u)# + getsizeof(u.__dict__)
print(size_u)

