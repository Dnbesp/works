# -*- coding: utf-8 -*-
# Завдання 1.
# Опишіть класи:
# 1) Гість, що містить інформацію про жильця деякого готелю: ім’я, період проживання, кількість грошей виділених
# на проживання.
# 2) Кімната містить інформацію про кімнату готелю у тому числі вартість проживання за добу, її доступність у
# визначений період (інформацію про те ким і коли вони зайняті тощо).
# 3) Готель (клас-менеджер) – містить список кімнат цього готелю, є посередником між гостем і кімнатою, тобто
# забезпечує для нього відповідну кімнату, тощо.
# Використовуючи вищенаведені класи розв’яжіть задачі:
# а) Про кількість вільних кімнат у готелі на вказаний момент;
# б) Пошуку вільної кімнати у зазначений період;
# в) Поселити жильця на вказаний термін;
# г) Вартості проживання жильця у зазначений період;
# д) Прибутку, який отримає готель за вказаний період;
# е) Пошуку гостя у готелі (у заданий період).

import datetime as datetime


class Guest:

    def __init__(self, name: str, date_guest_in: str, date_guest_out: str, money: int):
        self.name = name
        self.date_guest_in = datetime.datetime.strptime(date_guest_in, '%d/%m/%Y').date()
        self.date_guest_out = datetime.datetime.strptime(date_guest_out, '%d/%m/%Y').date()
        self.period_of_residence = (self.date_guest_out - self.date_guest_in).days
        self.money = money

    def __str__(self):
        return f"Ім'я: {self.name}, період проживання: {self.period_of_residence} (день/днів), " \
               f"ліміт грошей на проживання: {self.money}"


class Room:

    def __init__(self, number: int, bed: int, cost: int, date_busy_in=None, date_busy_out=None, guest_name=None):
        self.number = number
        self.bed = bed
        self.cost = cost
        self.guest_name = guest_name
        self.date_busy_in = datetime.datetime.strptime(date_busy_in, '%d/%m/%Y').date() if date_busy_in \
                                                                                           is not None else None
        self.date_busy_out = datetime.datetime.strptime(date_busy_out, '%d/%m/%Y').date() if date_busy_out \
                                                                                             is not None else None

    def __str__(self):
        return f'номер: {self.number}, ліжко: {self.bed}, дата заселення: {self.date_busy_in}, ' \
               f'дата виселення {self.date_busy_out}, ціна за добу: {self.cost} грн., гість: {self.guest_name}'


class Manager:
    total_profit = 0

    def __init__(self):
        self.guests_info = []
        self.rooms_info = []

    def add_guest(self, guest_inf: Guest):
        self.guests_info.append(guest_inf)

    def add_room(self, room_inf: Room):
        self.rooms_info.append(room_inf)

    def print_guest(self):
        for gue in self.guests_info:
            print(gue)

    def print_room(self):
        for roo in self.rooms_info:
            print(roo)

    def free_rooms(self, date_today: str):
        date_today = datetime.datetime.strptime(date_today, '%d/%m/%Y').date()
        count = 0
        for roo in self.rooms_info:
            if roo.date_busy_out is not None:
                if roo.date_busy_in < date_today:
                    count += 1
            count += 1
        return f'вільних кімнат: {count} на {date_today}'

    def found_free_room(self, date_in: str):
        date_in = datetime.datetime.strptime(date_in, '%d/%m/%Y').date()
        for roo in self.rooms_info:
            if roo.date_busy_out is not None:
                if date_in >= roo.date_busy_out:
                    print(f"вільний номер: '{roo.number}', на дату '{date_in}' з 14:00")
                else:
                    print(f"номер: '{roo.number}' занятий!")
            else:
                print(f"вільна кімната: '{roo.number}', на дату: '{date_in}' з 14:00")

    def settlement(self, name: str, number: int):
        for roo in self.rooms_info:
            if roo.number == number:
                for gue in self.guests_info:
                    if gue.name == name:
                        # перевірка необхідної суми на проживання і перевірка на достатність коштів
                        money = (roo.cost * (gue.date_guest_out - gue.date_guest_in)).days
                        if gue.money >= money:
                            if roo.date_busy_out is not None:
                                if gue.date_guest_in >= roo.date_busy_out:
                                    roo.guest_name = name
                                    roo.date_busy_in = gue.date_guest_in
                                    roo.date_busy_out = gue.date_guest_out
                                    Manager.total_profit += money
                                    print(f'гостя: {name} заселено в номер: {number}, сума до сплати = {money} грн.')
                                else:
                                    print(f'номер {number} на дати {gue.date_guest_in} - {gue.date_guest_out} '
                                          f'зайнятий!')
                            else:
                                roo.guest_name = name
                                roo.date_busy_in = gue.date_guest_in
                                roo.date_busy_out = gue.date_guest_out
                                Manager.total_profit += money
                                print(f'гостя: {name} заселено в номер: {number}, сума до сплати = {money} грн.')
                        else:
                            print(f'недостатньо коштів для заселення на вказаний період!')

    def cost_date(self, num_room: int, date_in: str, date_out: str):
        date_in = datetime.datetime.strptime(date_in, '%d/%m/%Y').date()
        date_out = datetime.datetime.strptime(date_out, '%d/%m/%Y').date()
        for num in self.rooms_info:
            if num.number == num_room:
                cost = (num.cost * (date_out - date_in)).days
                print(f"за проживання в номері '{num_room}' в період {date_in} - {date_out}, коштуватиме = {cost} грн.")

    def search_guest(self, nam):
        result = None
        for roo in self.rooms_info:
            if roo.guest_name == nam:
                result = f'гість {nam} знаходиться в номері {roo.number} в період {roo.date_busy_in} - ' \
                         f'{roo.date_busy_out}'
            if roo.guest_name != nam:
                continue
        if result is None:
            result = f'гостя {nam} немає в готелі!'
        return result


manager = Manager()
obj1 = Guest("Dmytro", '15/11/2023', '17/11/2023', 10000)
obj2 = Guest("Ivan", '17/11/2023', '20/11/2023', 8000)
obj3 = Guest("Evgen", '29/12/2023', '01/01/2024', 2000)
list_guest = [obj1, obj2, obj3]

for guest in list_guest:
    manager.add_guest(guest)

room1 = Room(101, 1, 700)
room2 = Room(102, 2, 850)
room3 = Room(103, 2, 1000)
list_room = [room1, room2, room3]

for room in list_room:
    manager.add_room(room)

# print(manager.free_rooms('22/11/2023'))
# manager.found_free_room('22/11/2023')
# manager.settlement("Ivan", 101)
# manager.print_room()
# print(manager.total_profit)
# manager.cost_date(103, '15/11/2023', '17/11/2023')

while True:

    print()
    print("1. Вивести інф. про гостів")
    print("2. Вивести інф. про кімнати")
    print("3. Вивести кількість вільних кімнат у готелі")
    print("4. Знайти вільні кімнати на вказану дату")
    print("5. Заселення гостя в номер")
    print("6. Підрахунок ціни за проживання в номері")
    print("7. Пошук гостя")
    print("8. Вивід прибутку готелю")
    print("0. Exit")

    cmd = int(input("Выберите пункт: "))

    if cmd == 1:
        manager.print_guest()
    if cmd == 2:
        manager.print_room()
    if cmd == 3:
        data = input("Введіть дату (d/m/y): ")
        print(manager.free_rooms(data))
    if cmd == 4:
        data = input("Введіть дату (d/m/y): ")
        manager.found_free_room(data)
    if cmd == 5:
        name = input("Введіть ім'я гостя: ")
        number = int(input("Введіть номер кімнати: "))
        manager.settlement(name, number)
    if cmd == 6:
        number = int(input("Введіть номер кімнати: "))
        date1 = input("Введіть дату заселення(d/m/y): ")
        date2 = input("Введіть дату виселення(d/m/y): ")
        manager.cost_date(number, date1, date2)
    if cmd == 7:
        name = input("Введіть ім'я гостя: ")
        print(manager.search_guest(name))
    if cmd == 8:
        print(manager.total_profit)
    if cmd == 0:
        break