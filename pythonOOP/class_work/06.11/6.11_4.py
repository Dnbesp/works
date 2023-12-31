def my_decorated(func):
    def wrapper(self):
        print("*"*10)
        func(self)
        print("*" * 10)

    return wrapper


class Test:

    def __init__(self, name):
        self.name = name

    @my_decorated
    def info(self):
        print(f"info: {self.name}")


t = Test("init")
t.info()