# 52
# class Money:
#     self.amount = 50
#     self.curency = 'USD'
#
# class BankAccount:
#     rate = {}
#     self.balance = Money(50, "USD")
#
#     @classmethod
#     def get_rate(cls):
#         text_json = json_from_(path)
#
#
# BankAccount.get_rate()
#
# bank1 = BankAccount(...)
# bank1.balance.amount
# bank1.balance.curency
#
# EU --> USD  EU --> UAN --> USD

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'<<{self.first_name} {self.last_name}'

class Baby(Person):
    def speak(self):
        print(f"{self.first_name} say: Blah blah blah")

class Adult(Person):
    def speak(self):
        print(f"My name is {self.first_name}")

class BatterPerson(Person):

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


p = Person("Jon", "Kirby")
p.first_name = "Jon2"
print(p.full_name)
b = Baby("Ivan", "Smith")
a = Adult("Alice", "Stoun")
# print(p, isinstance(p, Baby))
# print(b, isinstance(b, Baby))
b.speak()
a.speak()

p.full_name





