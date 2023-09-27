class Dog:
    def make_sound(self):
        print("Woof")

class Cat:
    def make_sound(self):
        print("Miaw")

class DogCat(Dog, Cat):
    def make_sound(self):
        for i in range(3):
            super(Dog, self).make_sound()

my_pet = DogCat()
my_pet.make_sound()

d = Dog()
c = Cat()

d.make_sound()
c.make_sound()

def get_sound(x):
    x.make_sound()

print()
get_sound(d)
get_sound(c)


