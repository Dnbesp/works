# Банківський рахунок                   Беспятий Дмитро
import json
import os

import requests


class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"


class BankAccount:
    account_number = 0
    balance = 100
    accounts = []
    __exchange_rate = {}

    def __init__(self, account_number, balance, owner_name, currency):
        self.account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        self.accounts.append(self)
        with open(f'data/account_number_{self.account_number}.txt', 'w') as file, open(f'data/account_number_{self.account_number}.txt', 'r+') as file1:
            text = file1.readline()
            text = "account_number balance currency owner_name" + '\n'
            file1.seek(0)
            file1.writelines(text)
            file1.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

    def __str__(self):
        return f'account_number: {self.account_number}, balance: {self.balance}, owner_name: {self.owner_name}'

    # Поповнення рахунку
    def deposit(self, balance):
        self.balance.amount += balance
        return f'Баланс поповнено! balance = {self.balance}'

    # Зняття з рахунку
    def withdraw(self, balance_draw):
        self.balance_draw = balance_draw
        if self.balance.amount > 0:
            if self.balance.amount - self.balance_draw < 0:
                return f"Помилка, у вас недостатньо коштів! Баланс = {self.balance}"
            else:
                self.balance = self.balance - self.balance_draw
                return f'З балансу знято {self.balance_draw}, Баланс = {self.balance}'
        else:
            return f"Помилка, на балансі '0'"

    # Зміна імені власника рахунку
    def change_owner_name(self, change_owner):
        # print(f'Власник рахунку: {self.owner_name}')
        self.owner_name = change_owner
        return f"Нове ім'я власника рахунку: {self.owner_name}"

    # Вивід повної інформації про рахунок
    def display_account_info(self):
        return (f"Номер рахунку: {self.account_number}, Баланс = {self.balance}, "
              f"Ім'я власника рахунку: {self.owner_name}")

    # Переказ коштів між рахунками
    def transfer(self, obj, value):
        try:
            self.obj = obj
            self.value = value
            # self.currency = currency
            print(f'Номер рахунку отримувача = {self.account_number}, balance = {self.balance.amount}, '
                  f'currency = {self.balance.currency}')
            print(f'Номер рахунку відправника = {self.obj.account_number}, balance = {self.obj.balance.amount}, '
                  f'currency = {self.obj.balance.currency}')
            print("-" * 45)
            if self.value < 0:
                raise
            else:
                if self.balance.currency == self.obj.balance.currency:
                    if self.obj.balance.amount >= self.value:
                        self.obj.balance.amount = self.obj.balance.amount - self.value
                        self.balance.amount = self.balance.amount + self.value
                        resalt = "Переказ успішний"
                    else:
                        resalt = "Значення переказу більше за баланс відправника"
                else:
                    resalt = "Переказ не можливий, різні валюти"
        except RuntimeError:
            resalt = "Значення переказу повинно бути бельше за 0"
        finally:
            print(f'Номер рахунку отримувача = {self.account_number}, balance = {self.balance.amount}, '
                  f'currency = {self.balance.currency}')
            print(f'Номер рахунку відправника = {self.obj.account_number}, balance = {self.obj.balance.amount}, '
                  f'currency = {self.obj.balance.currency}')
            print("-" * 45)

        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file2:
            text = file2.readline()
            text = "account_number balance currency owner_name" + '\n'
            file2.seek(0)
            file2.writelines(text)
            file2.writelines(f'{str(self.account_number)} {str(self.balance.amount)} {str(self.balance.currency)} '
                             f'{str(self.owner_name)} \n')

        with open(f'data/account_number_{self.obj.account_number}.txt', 'r+') as file2_1:
            text = file2_1.readline()
            text = "account_number balance currency owner_name" + '\n'
            file2_1.seek(0)
            file2_1.writelines(text)
            file2_1.writelines(f'{str(self.obj.account_number)} {str(self.obj.balance.amount)} {str(self.obj.balance.currency)} '
                             f'{str(self.obj.owner_name)} \n')

        return resalt

    # завантаження в __exchange_rate курси валют по відношенню до гривні
    @classmethod
    def create_exchange_rate(cls):
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        json_text = response.text
        BankAccount.__exchange_rate = json_text

    # трансфер у випадку різних валют
    def transfer_funds(self, target_account, amount):
        self.target_account = target_account
        self.amount = amount
        # print(BankAccount.__exchange_rate)
        json_text = json.loads(BankAccount.__exchange_rate)
        # print(json_text)
        if self.amount < self.target_account.balance.amount:
            for item in json_text:
                if item['cc'] == self.target_account.balance.currency:
                    send_money = round(item['rate'] * self.amount, 2)
                    print(f'Номер рахунку відправника = {self.target_account.account_number}, '
                          f'сума відправлення в грн.: {send_money}')
                    self.target_account.balance.amount -= amount
                    print(f'Номер рахунку відправника = {self.target_account.account_number}, '
                          f'balance = {self.target_account.balance.amount} {self.target_account.balance.currency}')
            for item in json_text:
                if item['cc'] == self.balance.currency:
                    take_money = round(send_money / item['rate'], 2)
                    self.balance.amount = round(self.balance.amount + take_money, 2)
                    print(f'Номер рахунку отримувача = {self.account_number}, '
                          f'поповнено на {take_money} {self.balance.currency}')
                    print(f'Номер рахунку отримувача = {self.account_number}, '
                          f'balance = {self.balance.amount} {self.balance.currency}')
        else:
            return f"Сума відправлення більше за залишок на рахунку"

        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file3:
            text = file3.readline()
            text = "account_number balance currency owner_name" + '\n'
            file3.seek(0)
            file3.writelines(text)
            file3.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

        with open(f'data/account_number_{self.target_account.account_number}.txt', 'r+') as file4:
            text = file4.readline()
            text = "account_number balance currency owner_name" + '\n'
            file4.seek(0)
            file4.writelines(text)
            file4.writelines(f'{str(self.target_account.account_number)} {str(self.target_account.balance)} '
                             f'{str(self.target_account.owner_name)} \n')
        return f"Операція успішна"


    # перевірка рахунку на валідність
    @staticmethod
    def check_account_number(account_number):
        if len(str(account_number)) == 5:
            return f"Номер рахунку є валідним"
        else:
            return f"Номер рахунку не є валідним"

    # getter
    @property
    def account_number(self):
        return self.__account_number

    # setter
    @account_number.setter
    def account_number(self, account_number):
        # print(self.__account_number)
        self.__account_number = account_number
        # print(self.__account_number)

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        count = 0
        for account in cls.accounts:
            if account.owner_name == owner_name:
                count += 1
                # matching_accounts.append(account.account_number)
                # matching_accounts.append(account.balance.amount)
                # matching_accounts.append(account.balance.currency)
                matching_accounts.append(owner_name)
        print(count)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total_balance = 0
        count = 0
        for account in cls.accounts:
            count += 1
            total_balance += account.balance.amount
        return int(total_balance / count)

    def delete(self, account_number):
        self.account_number = account_number
        os.remove(f'data/account_number_{self.account_number}.txt')



# Mon_1 = Money(2100, 'USD')
# Mon_2 = Money(5000, 'USD')
Dm = BankAccount(12567, 2100, 'Dmytro', "USD")
# N = BankAccount(13245, 5000, 'Nats', "EUR")
# Dm.delete(12567)


Dm.create_exchange_rate()
# Dm.transfer_funds(N, 100)
# for item in Dm.accounts:
#     print(item)
# print(N.transfer(Dm, 100))
# # print()
# print(Dm.transfer(N, 5300))
# print(BankAccount.get_average_balance())
# print(BankAccount.find_accounts_by_owner('Dmytro'))


# print(Dm.deposit(1000))
# print(N.deposit(500))
# print(Dm.withdraw(3000))
# print(Dm.withdraw(900))
# print(N.withdraw(5600))
# print(N.withdraw(100))
# print(Dm.change_owner_name('Nik'))
# print(N.change_owner_name('Ketch'))
# Dm.display_account_info()
# N.display_account_info()
# print(Dm.transfer(N, -1))
# print()
# print(N.transfer(Dm, 100))
# print()
# print(Dm.transfer(N, 5300))
# Dm.check_account_number(12567)
# BankAccount.check_account_number(132451)
# print(Dm.get_account_number())
# print(N.get_account_number())
# Dm.set_account_number(11111)
# N.set_account_number(22222)
# print(Dm.get_account_number)
# print(N.get_account_number)
# print(Dm)
# print(N)
# Dm.account_number = 11111
# N.account_number = 22222
# print(Dm)
# print(N)
