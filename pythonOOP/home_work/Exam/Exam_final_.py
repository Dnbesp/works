
import datetime as DT


class GuestHotel:

    """Гість, що містить інформацію про жильця деякого готелю: ім'я, період проживання, кількість грошей
    виділених на проживання."""

    def __init__(self, name, date_settlement, date_eviction, money):
        self.name = name
        self.date_settlement = DT.datetime.strptime(date_settlement, '%d/%m/%Y').date()
        self.date_eviction = DT.datetime.strptime(date_eviction, '%d/%m/%Y').date()
        self.period_of_residence = self.date_eviction - self.date_settlement
        self.period_of_residence = self.period_of_residence.days
        self.money = money
        self.gust_info = []

    def __str__(self):
        return f"Ім'я: {self.name}, період проживання: {self.period_of_residence} (день/днів), " \
               f"ліміт грошей на проживання: {self.money}"

    # запис гістя в історію готелю
    def write_gust(self):
        self.gust_info.append(f"{self.name} {self.date_settlement} {self.date_eviction} {self.period_of_residence} "
                              f"{obj.money}")



# Ввід і вивід інформації про гістя
class Console:

    # @staticmethod
    # def display(obj: GuestHotel):
    #     print(f"Ім'я: {obj.name}, заселення в період: {obj.date_settlement} - {obj.date_eviction}, "
    #           f"ліміт грошей на проживання: {obj.money}")
    #
    # @staticmethod
    # def input():
    #     name = input("Input name guest: ")
    #     date_settlement = input("Input date of settlement (format: 15/11/2023): ")
    #     date_eviction = input("Input date of eviction (format: 15/11/2023): ")
    #     money = int(input("Input limit money: "))
    #     return GuestHotel(name, date_settlement, date_eviction, money)


class RoomInfo:

    """Інформація щодо кімнат в Готелі"""

    # def __init__(self, number, num_of_rooms='1', bed='1', date_busy_in=None, date_busy_out=None, cost='0'):
    #     self.number = number
    #     self.num_of_rooms = num_of_rooms
    #     self.bed = bed
    #     if date_busy_in is not None:
    #         self.date_busy_in = DT.datetime.strptime(date_busy_in, '%d/%m/%Y').date()
    #     else:
    #         self.date_busy_in = date_busy_in
    #     if date_busy_out is not None:
    #         self.date_busy_out = DT.datetime.strptime(date_busy_out, '%d/%m/%Y').date()
    #     else:
    #         self.date_busy_out = date_busy_out
    #     self.cost = cost
    #
    # def __str__(self):
    #     return f'номер: {self.number}, кількість кімнат: {self.num_of_rooms}, ліжко: {self.bed}, ' \
    #            f'дата заселення: {self.date_busy_in}, дата виселення {self.date_busy_out}, ціна за добу: {self.cost} грн.'
    #
    # # запис інформації за номери в файл rooms.txt
    # def writer_room(self):
    #     self.data = f'{self.number} | {self.num_of_rooms} | {self.bed} | {self.date_busy_in} | ' \
    #                 f'{self.date_busy_out} | {self.cost} '
    #     with open('rooms.txt', 'r+') as f:
    #         lines = f.readlines()
    #         f.seek(0)
    #
    #     with open('rooms.txt', 'a+') as f2:
    #         if self.data not in read_rom:
    #             for room in read_rom:
    #                 room = room.split()
    #                 if room[0] == self.number:
    #                     del room
    #                     f2.writelines(f'{self.data}\n')


# зміна ціни за номер кімнати
# class CostRooms(RoomInfo):
#
#     def __init__(self, number, cost):
#         super().__init__(number, cost)
#         self.number = number
#         self.cost = cost
#
#     def __str__(self):
#         return f'номер: {self.number}, {self.num_of_rooms} ціна за добу: {self.cost} грн.'
#
#     # запис ціни в файл rooms.txt
#     def data(self):
#         print(self.number, self.num_of_rooms, self.cost)
#         return super().writer_room()
#
#
# # перевірка кількості вільних кімнат
# class FreeRoom:
#
#     def free_rooms(self):
#         with open('rooms.txt') as f:
#             free = f.readlines()
#             count = 0
#             for rom in free:
#                 rom = rom.split()
#                 if rom[-3] == None:
#                     print(*rom)
#                     count += 1
#                 else:
#                     continue
#             if count == 0:
#                 print(f'вільних номерів не знайдено!')
#
#     # вільні кімнати в певну дату
#     # def date_free_rooms(self):
#
#
# class RoomHotel:
#
#     """Кімната містить інформацію про кімнату готелю у тому числі вартість проживання за добу, її доступність
#     у визначений період (інформацію про те ким і коли вони зайняті тощо."""
#
#     def __init__(self, number_room):
#         self.number_room = number_room
#
#     def search_info(self):
#         with open('rooms.txt') as f, open('price_room.txt') as f2:
#             read_rom = f.readlines()
#             read_price_rom = f2.readlines()
#             for rom in read_rom:
#                 rom = rom.split()
#                 if rom[1] == self.number_room:
#                     rez_search = rom
#                     break
#                 else:
#                     print(f'Комнати з номером {self.number_room} не знайдено!')
#             for rom in read_price_rom:
#                 rom = rom.split()
#                 if rom[1] == self.number_room:
#                     rez_search_price = rom
#                     break
#                 else:
#                     print(f'Комнати з номером {self.number_room} не знайдено!')
#         return f'Пошук завершено: {rez_search}\n                 {rez_search_price}'
#
# class ManagerHotel:
#
#     """Готель - містить список кімнат цого готелю, є посередником між гостем і кімнатою, тобто забезпечує для
#     нього відповідну кімнату, тощо."""
#
#     # кількість всього номерів у готелі
#     def count_rom(self):
#         with open('rooms.txt') as f:
#             count_rom = f.readlines()
#             count = 0
#             for rom in count_rom:
#                 count += 1
#             print(f'всього номерів у готелі: {count}')
#
#     # пошук вільного номера
#     def search_for_guest(self):
#         with open("rooms.txt") as f:
#             room_for_guest = f.readlines()
#             for rom in room_for_guest:
#                 rom = rom.split()
#                 if rom[-1] == "No":
#                     self.free_room = rom[1]
#                     break
#                 else:
#                     self.free_room = 0
#             if self.free_room == 0:
#                 print("вільного номенра не знайдено")
#             return self.free_room

    # заселення в номер:
    # def settlement(self):
    #     with open('gust_in_hotel.txt') as f, open('gust_in_hotel.txt', 'a+') as f2:
    #         read_gust = f.read()
    #         if self.free_room != 0:
    #             with open('gust_in_hotel.txt')

    # def cost_for_liv(self):



obj = GuestHotel("Dmytro", '15/11/2023', '17/11/2023', '1000')
obj2 = GuestHotel("Ivan", '17/11/2023', '20/11/2023', '800')
obj.write_gust()
obj2.write_gust()
# Console.display(obj)
# new_guest = Console.input()
# Console.display(new_guest)

# інформація про номер і запис у файл
# room_1 = RoomInfo('101', '1', '1')
# room_1.writer_room()
# room_2 = RoomInfo('102', '2', '2')
# room_2.writer_room()
# room_3 = RoomInfo('103', '2', '3')
# room_3.writer_room()

#зміна ціни за номер
# cost_101 = CostRooms('101', '500')
# print(cost_101)
# # cost_101.price_room()
# cost_101.data()
# cost_102 = CostRooms('102', '600')
# cost_102.data()
# # cost_102.price_room()
# cost_103 = CostRooms('103', '1000')
# cost_103.data()
# cost_103.price_room()
#
# room_hot = RoomHotel('10')
# print(room_hot.search_info())
#
# fre = FreeRoom()
# fre.free_rooms()
#
# manager = ManagerHotel("Dmytro", '15/11/2023', '17/11/2023', 1000, "UAH", 10, 500, "UAH")
# # manager.count_rom()
# print(manager.search_for_guest())
# manager.settlement()