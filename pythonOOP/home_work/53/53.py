# task 1                    Беспятий Дмитро

# Визначте три класи: Printer, Lamp і Car. Кожен з них має тільки один метод does(). Він повертає значення 'print'
# (для Printer), 'glow' (для Lamp) або 'ride' (для Car). Далі визначте клас Robot з методом __init__, який містить
# по одному екземпляру кожного з цих класів як власні атрибути. Визначте метод do_it() для класу Robot, який виводить
# на екран усі дії, що роблять його компоненти.

# class Printer:
#
#     def does(self, print):
#         self.print = print
#         return self.print
#
# class Lamp:
#
#     def does(self, glow):
#         self.glow = glow
#         return self.glow
#
# class Car:
#
#     def does(self, ride):
#         self.ride = ride
#         return self.ride
#
# class Robot:
#
#     def __init__(cls, p, l, c):
#         cls.p = p
#         cls.l = l
#         cls.c = c
#
#     def do_it(self):
#         print(p.does)
#         print(l.does)
#         print(c.does)
#
#
# p = Printer()
# l = Lamp()
# c = Car()
# r = Robot(p, l, c)
# r.do_it()


# task 2                    Беспятий Дмитро

# Створіть ієрархію класів для представлення осіб з різними характеристиками, використовуючи клас `Person` як
# батьківський клас.
# 1. Створіть клас `Person` з атрибутами `name` і `age`. Реалізуйте метод __init__. Додайте також метод
# `introduce()`, який виводить ім'я та вік особи.
# 2. Створіть клас `Student`, який успадковує клас `Person`. Додайте атрибут ` id` при ініціалізації об’єкта
# (перевизначте метод __init__, в якому буде викликатись за допомогою super батьківський __init__).
# Додайте метод `study(subject)`, який виводить повідомлення, що студент {self.name}-{self.id} навчається предмету
# subject.
# 3. Створіть клас `Teacher`, який успадковує клас `Person`. Додайте атрибут `subject` та метод ` teach(s)`, який
# виводить повідомлення, що «викладач {self.name} навчає {self.subject} студента {s.name}», де s – це деякий екземпляр
# Student. У методі teach зробіть перевірку чи s є дійсно об`єктом з класу Student, якщо ні, то вивести відповідне
# повідомлення.
# 4. Створіть клас `Employee`, який успадковує клас `Person`. Додайте атрибути salary, specialty та метод `work()`,
# який виводить повідомлення про роботу співробітника та його зарплату.
# 5. Створіть по одному об'єкту кожного з класів `Student`, `Teacher`, `Employee` і викличте методи, що відповідають
# їхній ролі. Протестуйте роботу методів, що задаються у них
# 6. Перевизначте метод ` introduce()` у класах `Student`, `Teacher`, `Employee`, щоб вони давали всю інформацію про
# особу та назву класу, до якого вона відноситься. Протестуйте роботу.

# class Person:
#     name = ''
#     age = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f'name: {self.name}, age: {self.age}')
#
#
# class Student(Person):
#     id = 0
#
#     def __init__(self, name, age, id):
#         super().__init__(name, age)
#         self.id = id
#
#     def study(self, subject):
#         self.subject = subject
#         print(f'Студент {self.name}-{self.id} навчається предмету {self.subject}')
#
#     def introduce(self):
#         print(f'name: {self.name}, id: {self.id}, age: {self.age}, name class: {__class__.__name__}')
#
#
# class Teacher(Person):
#     subject = ''
#
#     def teach(self, name, subject, st):
#         self.name = name
#         self.subject = subject
#         self.st = st
#         if st == s.name:
#             print(f'викладач {self.name} навчає {self.subject} студента {st}')
#         else:
#             print(f'викладач {self.name} навчає {self.subject} нового студента {st}')
#
#     def introduce(self):
#         print(f'name: {self.name}, subject: {self.subject}, name class: {__class__.__name__}')
#
#
# class Employee(Person):
#     salary = 0
#     specialty = ''
#
#     def work(self, salary, specialty):
#         self.salary = salary
#         self.specialty = specialty
#         print(f'specialty: "{self.specialty}", salary: {self.salary}')
#
#     def introduce(self):
#         print(f'salary: {self.salary}, specialty: {self.specialty}, name class: {__class__.__name__}')

#1
# p = Person("Dima", 35)
# p.introduce()
#2
# p = Person("Dima", 35)
# s = Student("Dima", 36, 345)
# s.study("English")
#3
# s = Student("Dima", 36, 345)
# t = Teacher("Dima", 35)
# t.teach("Eva", "English", "Roma")
#4
# e = Employee("Dima", 35)
# e.work(1000, 'programmer')
#6
# s = Student("Dima", 36, 345)
# t = Teacher("Ann", 35)
# e = Employee("Dima", 35)
# e.work(1000, 'programmer')
# s.introduce()
# t.introduce()
# e.introduce()


# task 3                    Беспятий Дмитро


import datetime


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Baby(Person):
    def speak(self):
        print('Blah blah blah')


class Adult(Person):
    def speak(self):
        print('Hello, my name is', self.first_name)


class Calendar:
    def book_appointment(self, date):
        print('Booking appointment for date', date)


class OrganizedAdult(Adult, Calendar):
    pass


class OrganizedBaby(Baby, Calendar):
    pass


andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018, 1, 1))


class OrganizedBaby(Baby, Calendar):
    def book_appointment(self, date):
        print('Note that you ara booking an appointment whith a baby.')
        super().book_appointment(date)

boris = OrganizedBaby('Boris', 'Bumblebutton')
boris.book_appointment(datetime.date(2018, 1, 1))






