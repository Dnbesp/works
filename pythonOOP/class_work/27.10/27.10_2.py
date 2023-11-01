from copy import copy, deepcopy


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __str__(self):
        return f"Address ({self.street} {self.city})"

class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Person {self.name} lives at {self.address}"

    def clone(self, name=''):
        name = name if name is not None else self.name
        address = deepcopy(self.address)
        return self.__class__(name, address)



address = Address("123 Road", "London")
john = Person("John", address)
print(john)
jane = Person("Jane", address)
print(jane)
print("___")
#jane = deepcopy(john)
jane = john.clone("Jane")
john.address.street = "100 Road"

print(jane)
print(john)

