# task 1                    Беспятий Дмитро
class Person:

    '''Опис класу.
        Ці рядки автоматично можна продивитись функцією help'''

    def __init__(self, name='xxx', money=0):
        self.name = name
        self.money = money
        self.friends = []
        print('A new Person is born! ->', self.name)

    def __str__(self):
        return self.name + ' ' + str(self.money)

    def __repr__(self):
        return f'Person({self.name})'

    def giveMoney(self, delta):
        self.money += delta
        print('Рахунок {} поповнено на суму {}, всього = {}'
              .format(self.name, delta, self.money))

    def know(self, person):
        if person in self.friends:
            print("Така персона вже є у сприску")
        else:
            self.friends.append(person)
            person.friends.append(self)
            print("Персона додана")

    def is_know(self, person):
        if person in self.friends:
            return f'He is familiar'
        else:
            return f'He is not familiar'

A = Person()
B = Person()
C = Person('Petro', 10)
D = Person('Ira', 30)

print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))

A.name = 'Ivan'
B.name = 'Anna'
B.money = 100.2852

A.giveMoney(50.127)
B.giveMoney(40)

print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))

def info(person):
    i = person.name + str(person.money)
    return i

people = [A,B,C,D]

for p in people:
    print(info(p))

print('-' * 50)

# help(Person)

def min_num(person):
    if person.money < 50:
        person.money += 100
    return person.name + ' - ' + str(person.money)

for p in people:
    print(min_num(p))

print('-' * 50)

A.know(C)
A.know(B)

print(A.friends)
print(C.friends)

print(A.is_know(C))
print(A.is_know(D))


