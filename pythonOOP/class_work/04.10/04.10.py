class NameDescriptor:

    def __init__(self, prefix="_", lenght = 5):
        self.prefix = prefix
        self.lenght = lenght

    def __set_name__(self, owner, name):
        var_name = self.prefix + name
        self.var = var_name


    def __set__(self, instance, value):
        if len(value) >= 5:
            setattr(instance, self.var, value)
        else:
            raise ValueError


    # def __set__(self, instance, value):
    #     setattr(instance, self.var, value)
    #     print("Call User")
        # instance.__dict__[self.var] = value

    def __get__(self, instance, owner):
        return getattr(instance, self.var)
        # return instance.__dict__[self.var]


class User:
    username = NameDescriptor(prefix="__")
    name = NameDescriptor(prefix="__", lenght=2)
    last_name = NameDescriptor(lenght=3)

    def __init__(self, username, name, last_name):
        self.username = username
        self.name = name
        self.last_name = last_name

u = User("admin", "Jon", "Col")
print(u.__dict__)
print(u.username, u.name, u.last_name)