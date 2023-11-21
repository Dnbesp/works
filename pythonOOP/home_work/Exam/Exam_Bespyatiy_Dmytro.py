import datetime as DT


class GuestHotel:

    """Гість, що містить інформацію про жильця деякого готелю: ім'я, період проживання, кількість грошей
    виділених на проживання."""

    def __init__(self, name, date_settlement, date_eviction, money):
        self.name = name
        self.date_settlement = DT.datetime.strptime(date_settlement, '%d/%m/%Y').date()
        self.date_eviction = DT.datetime.strptime(date_eviction, '%d/%m/%Y').date()
        self.period_of_residence = (self.date_eviction - self.date_settlement)
        self.period_of_residence = self.period_of_residence.days
        self.money = money
        self.info_guest = []
        self.info_guest.append(f"{self.name} | {self.date_settlement} | {self.date_eviction} | "
                               f"{self.period_of_residence} | {self.money}")

    def __str__(self):
        return f"Ім'я: {self.name}, період проживання: {self.period_of_residence} (день/днів), " \
               f"ліміт грошей на проживання: {self.money}"


class RoomInfo:
    """Кімната містить інформацію про кімнату готелю у тому числі вартість проживання за добу, її доступність у
    визначений період (інформацію про те ким і коли вони зайняті тощо)"""

    def __init__(self, number, num_of_rooms=1, bed=1, date_busy_in=None, date_busy_out=None, cost=0, guest=None):
        self.number = number
        self.num_of_rooms = num_of_rooms
        self.bed = bed
        if date_busy_in is not None:
            self.date_busy_in = DT.datetime.strptime(date_busy_in, '%d/%m/%Y').date()
        if date_busy_in is None:
            self.date_busy_in = date_busy_in
        if date_busy_out is not None:
            self.date_busy_out = DT.datetime.strptime(date_busy_out, '%d/%m/%Y').date()
        if date_busy_out is None:
            self.date_busy_out = date_busy_out
        self.cost = cost
        self.guest = guest
        self.room_info = []
        self.room_info.append('{} {} {} {} {} {} {}'.format(self.number, self.num_of_rooms, self.bed, self.date_busy_in,
                                                            self.date_busy_out, self.cost, self.guest))

    def __str__(self):
        return f'номер: {self.number}, кількість кімнат: {self.num_of_rooms}, ліжко: {self.bed}, дата заселення: ' \
               f'{self.date_busy_in}, дата виселення {self.date_busy_out}, ціна за добу: {self.cost} грн., ' \
               f'гість {self.guest}'

    # перевірка кількості вільних кімнат
    def free_rooms(self):
        count = 0
        for room in self.room_info:
            room = room.split()
            if room[-3] is None:
                count += 1
            else:
                continue
        if count == 0:
            print(f'номер {self.number} зайнятий з {self.date_busy_in} по {self.date_busy_out}!!!')
        if count > 0:
            print(f'вільний номер: {self.number}')

    # перевірка кількості вільних кімнат у вказаний період
    def data_free_rooms(self, data_1, data_2):
        self.data_1 = DT.datetime.strptime(data_1, '%d/%m/%Y').date()
        self.data_2 = DT.datetime.strptime(data_2, '%d/%m/%Y').date()
        if self.date_busy_out is not None:
            if self.data_1 >= self.date_busy_out:
                print(f'на даний момент номер {self.number} зайнятий, але буде вільний {self.date_busy_out} '
                      f'з 12 години.')
            if self.data_2 < self.date_busy_in:
                print(f'номер {self.number} вільний до {self.date_busy_in}')
        if self.date_busy_out is None:
            print(f'на даний момент номер {self.number} вільний')

    # вартість проживання у зазначений термін
    def cost_date(self, data_1, data_2):
        self.data_1 = DT.datetime.strptime(data_1, '%d/%m/%Y').date()
        self.data_2 = DT.datetime.strptime(data_2, '%d/%m/%Y').date()
        cost_dates = self.cost * (self.data_2 - self.data_1).days
        print(f'ціна за проживання з {self.data_1} по {self.data_2} в номері {self.number} складає: {cost_dates}')

    # знайти в якій кімнаті гість
    def find_guest(self, name_find):
        self.name_find = name_find
        if self.name_find == self.guest:
            print(f'гість: {self.name_find} знаходиться в кімнаті {self.number}')
        else:
            print(f'гість: {self.name_find} не знаходиться в готелі')


class ManagerHotel(GuestHotel, RoomInfo):

    """Готель - містить список кімнат цого готелю, є посередником між гостем і кімнатою, тобто забезпечує для
        нього відповідну кімнату, тощо."""

    total_profit = 0

    def __init__(self, number, date_busy_in, date_busy_out, cost, guest, name, date_settlement, date_eviction, money):
        super(GuestHotel, self).__init__(number, date_busy_in, date_busy_out, cost, guest)
        super(RoomInfo, self).__init__(name, date_settlement, date_eviction, money)

    def __str__(self):
        return f'{self.number} {self.date_busy_in} {self.date_busy_out} {self.cost} {self.guest} {self.name}' \
               f' {self.date_settlement} {self.date_eviction} {self.money}'

    # заселення в номер:
    def settlement(self):
        # перевірка по даті виселення, кімната пуста чи ні
        if self.date_busy_out is not None:

            # перевірка чи більше, або співпадає дата заселення гістя по відношенню до дати виселення с номера
            if self.date_settlement >= self.date_busy_out:
                days_cost = self.cost * (self.date_eviction - self.date_settlement).days

                # перевірка чи достатньо грошей в гістя
                if self.money >= self.cost and self.money >= days_cost:
                    self.date_busy_in = self.date_settlement
                    self.date_busy_out = self.date_eviction
                    self.guest = self.name
                    print(f'гість {self.name} посилився у номер {self.number}')
                    print(self.room_info)
                    ManagerHotel.total_profit += days_cost
                else:
                    raise ValueError("Не вистачає коштів у гістя для приживання в даному номері")
        if self.date_busy_out is None:
            days_cost = self.cost * (self.date_eviction - self.date_settlement).days
            if self.money >= self.cost and self.money >= days_cost:
                self.date_busy_in = self.date_settlement
                self.date_busy_out = self.date_eviction
                self.guest = self.name
                print(f'гість {self.name} посилився у номер {self.number}')
                print(self.room_info)
                ManagerHotel.total_profit += days_cost
            else:
                raise ValueError("Не вистачає коштів у гістя для приживання в даному номері")


# клас GuestHotel(вся інформація пов'язана з гостем)
obj = GuestHotel("Dmytro", '15/11/2023', '17/11/2023', 1000)
obj2 = GuestHotel("Ivan", '17/11/2023', '20/11/2023', 800)

# клас RoomInfo(вся інформація пов'язана з номером)
room_1 = RoomInfo(101, 1, 1, "15/11/2023", '19/11/2023', 500)
room_2 = RoomInfo(102, 2, 2, "16/11/2023", '27/11/2023', 800)
room_3 = RoomInfo(103, 1, 3, "16/11/2023", '20/11/2023', 1000)

# перевірка кількості вільних кімнат на зараз
# room_1.free_rooms()
# room_2.free_rooms()
# room_3.free_rooms()

# перевірка кількості вільних кімнат у вказаний період
# room_1.data_free_rooms("19/11/2023", '20/11/2023')
# room_2.data_free_rooms("17/11/2023", '20/11/2023')
# room_3.data_free_rooms("21/11/2023", '25/11/2023')

# вартість проживання у зазначений термін
room_1.cost_date("19/11/2023", '20/11/2023')
room_2.cost_date("17/11/2023", '20/11/2023')
room_3.cost_date("21/11/2023", '25/11/2023')

# знайти в якій кімнаті гість
# room_1.find_guest("Dmytro")
# room_2.find_guest("Ivan")
#
# manager_1 = ManagerHotel(2, "16/11/2023", '27/11/2023', 800, None, "Dmytro", '15/11/2023', '17/11/2023', 1000)
# manager_2 = ManagerHotel(1, "15/11/2023", '19/11/2023', 500, None, "Ivan", '17/11/2023', '20/11/2023', 800)

# заселення в номер:
# manager_1.settlement()
# manager_2.settlement()
# room_1.free_rooms()
# room_2.free_rooms()
# room_3.free_rooms()

# вивід загального прибутку Готелю
# print(ManagerHotel.total_profit)
