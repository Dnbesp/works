# !/usr/bin/python
#  vim: set fileencoding=<UTF-8> :

import datetime as DT

class GuestHotel:

    """ó���, �� ������ ���������� ��� ������ ������� ������: ��'�, ����� ����������, ������� ������
    �������� �� ����������."""

    def __init__(self, name, date_settlement, date_eviction, money):
        self.name = name
        self.date_settlement = DT.datetime.strptime(date_settlement, '%d/%m/%Y').date()
        self.date_eviction = DT.datetime.strptime(date_eviction, '%d/%m/%Y').date()
        self.period_of_residence = self.date_eviction - self.date_settlement
        self.period_of_residence = self.period_of_residence.days
        self.money = money
        self.gust_info = []

    def __str__(self):
        return f"��'�: {self.name}, ����� ����������: {self.period_of_residence} (����/���), " \
               f"��� ������ �� ����������: {self.money}"

    # ����� ���� � ������ ������
    def write_gust(self):
        self.gust_info.append(f"{self.name} {self.date_settlement} {self.date_eviction} {self.period_of_residence} "
                              f"{obj.money}")


obj = GuestHotel("Dmytro", '15/11/2023', '17/11/2023', '1000')
obj2 = GuestHotel("Ivan", '17/11/2023', '20/11/2023', '800')
obj.write_gust()
obj2.write_gust()