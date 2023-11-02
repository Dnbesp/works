from abc import ABC, abstractmethod

# Define an abstract base class (ABC) for Bird with two abstract methods
class WalkAble(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyAble(ABC):
    def fly(self):
        pass


class EatAble:
    def eat(self):
        print(f"Їсти! {self.__class__.__name__}")


class Ostriche(WalkAble, EatAble):
    def walk(self):
        print("Ostriche is walking")


class Eagle(WalkAble, FlyAble, EatAble):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")


try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj.eat()
    obj2 = Ostriche()
    obj2.walk()
    obj2.eat()


    # Will raise an exception as ostriches can't fly
    obj2.fly()
except Exception as e:
    # Print the exception message
    print(e)