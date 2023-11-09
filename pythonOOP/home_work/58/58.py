# task 1                                     Беспятий Дмитро

class Size:

    def __get__(self, obj, objtype=None):
        return len(getattr(obj, 'name'))


class Person:
    size_name = Size()

    def __init__(self, name):
        self.name = name


# p = Person('itstep')
# print(p.size_name)


# task 2                                     Беспятий Дмитро

class UsernameDescriptor:

    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if not value[0].isdigit() and 4 <= len(value) <= 10:
            instance._username = value
        else:
            raise ValueError("The first character of the name must be a letter. "
                             "Length from 4 to 10 characters.")


class PasswordDescriptor:

    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if len(str(value)) >= 8:
            instance._password = value
        else:
            raise ValueError("The length of the password is less than 8 characters")


class User:
    username = UsernameDescriptor()
    password = PasswordDescriptor()

    def __init__(self, username, password):
        self.username = username
        self.password = password


us = User("Dima", 12345678)
print(us.username)
print("--------------")
us.username = 'Ivan'
print(us.username)
print("--------------")
print(us.password)
print("--------------")
us.password = '123ytr987567'
print(us.password)
# us.username = '5Ivan'
# us.password = '123ytr'

