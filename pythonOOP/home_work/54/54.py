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
        with open(f'data/account_number_{self.account_number}.txt', 'w') as file, \
                open(f'data/account_number_{self.account_number}.txt', 'r+') as file1:
            text = file1.readline()
            text = "account_number balance currency owner_name" + '\n'
            file1.seek(0)
            file1.writelines(text)
            file1.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

    def __str__(self):
        return f'account_number = {self.account_number}, balance = {self.balance}'

    # Поповнення рахунку
    def deposit(self, balance):
        self.balance += balance
        return f'Баланс поповнено! balance = {self.balance}'

    # Зняття з рахунку
    def withdraw(self, balance_draw):
        self.balance_draw = balance_draw
        if self.balance.amount > 0:
            if self.balance.amount - self.balance_draw < 0:
                return f"Помилка, у вас недостатньо коштів! Баланс = {self.balance}"
            else:
                if NewBankAccount.count < self.max_count_transaction:
                    if self.max_limit > self.balance_draw:
                        self.balance.amount = self.balance.amount - self.balance_draw
                        NewBankAccount.count += 1
                        return f'З балансу знято {self.balance_draw}, Баланс = {self.balance}'
                    else:
                        return(f'Введена сума більше за максимальний розмір для зняття')
                else:
                    return(f'Перевищено максимальну кількість операцій з рахунком')
        else:
            return f"Помилка, на балансі '0'"

    # Зміна імені власника рахунку
    def change_owner_name(self, change_owner):
        print(f'Власник рахунку: {self.owner_name}')
        self.owner_name = change_owner
        return f"Нове ім'я власника рахунку: {self.owner_name}"

    # Вивід повної інформації про рахунок
    def display_account_info(self):
        print(f"Номер рахунку: {self.account_number}, Баланс = {self.balance}, "
              f"Ім'я власника рахунку: {self.owner_name}")

    # Переказ коштів між рахунками
    def transfer(self, obj, value):
        try:
            self.obj = obj
            self.value = value
            print(f'Номер рахунку отримувача = {self.account_number}, balance = {self.balance.amount}, '
                  f'currency = {self.balance.currency}')
            print(f'Номер рахунку відправника = {self.obj.account_number}, balance = {self.obj.balance.amount}, '
                  f'currency = {self.obj.balance.currency}')
            print("-" * 45)
            if self.value < 0:
                raise
            else:
                if NewBankAccount.count < self.max_count_transaction:
                    if self.max_limit > self.value:
                        if self.balance.currency == self.obj.balance.currency:
                            if self.obj.balance.amount >= self.value:
                                self.obj.balance.amount = self.obj.balance.amount - self.value
                                self.balance.amount = self.balance.amount + self.value
                                NewBankAccount.count += 1
                                resalt = "Переказ успішний"
                            else:
                                resalt = "Значення переказу більше за баланс відправника"
                        else:
                            resalt = "Переказ не можливий, різні валюти"
                    else:
                        return(f'Введена сума більше за максимальний розмір для зняття')
                else:
                    return(f'Перевищено максимальну кількість операцій з рахунком')

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
        cls.__exchange_rate = json_text

    # трансфер у випадку різних валют
    def transfer_funds(self, target_account, amount):
        self.target_account = target_account
        self.amount = amount
        json_text = json.loads(self.__exchange_rate)
        if NewBankAccount.count < self.max_count_transaction:
            if self.max_limit > self.amount:
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
                            NewBankAccount.count += 1
                else:
                    print("Сума відправлення більше за залишок на рахунку")
            else:
                print(f'Введена сума більше за максимальний розмір для зняття')
        else:
            print(f'Перевищено максимальну кількість операцій з рахунком')

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


    # перевірка рахунку на валідність
    @staticmethod
    def check_account_number(account_number):
        if len(str(account_number)) == 5:
            print("Номер рахунку є валідним")
        else:
            print("Номер рахунку не є валідним")

    # getter
    @property
    def account_number(self):
        return self.__account_number

    @property
    def exchange_rate(self):
        return self.__exchange_rate

    # setter
    @account_number.setter
    def account_number(self, account_number):
        # print(self.__account_number)
        self.__account_number = account_number
        # print(self.__account_number)


    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account['owner_name'] == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total_balance = 0
        for account in cls.accounts:
            total_balance += account['balance']
        return int(total_balance / BankAccount.count)

    def delete(self, account_number):
        self.account_number = account_number
        os.remove(f'data/account_number_{self.account_number}.txt')


class NewBankAccount(BankAccount):
    count = 0

    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transaction):
        super().__init__(account_number, balance, owner_name, currency)
        self.max_limit = max_limit
        self.max_count_transaction = max_count_transaction

    def prosent(self, pros):
        self.pros = pros
        self.balance.amount = int(self.balance.amount + (self.balance.amount * (self.pros / 100)))
        print(f'account_number: {self.account_number}, balance: {self.balance.amount} {self.balance.currency}')

        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file5:
            text = file5.readline()
            text = "account_number balance currency owner_name" + '\n'
            file5.seek(0)
            file5.writelines(text)
            file5.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file6:
            text = file6.readline()
            text = "account_number balance currency owner_name" + '\n'
            file6.seek(0)
            file6.writelines(text)
            file6.writelines(f'{str(self.account_number)} {str(self.balance)} '
                             f'{str(self.owner_name)} \n')



new = NewBankAccount(12567, 2100, 'Dmytro', "USD", 300, 2)
new_2 = NewBankAccount(13456, 3100, 'Ivan', "EUR", 700, 3)
new.prosent(15)





# трансфер у випадку різних валют
# new.create_exchange_rate()
# new.transfer_funds(new_2, 200)
# print()
# new.transfer_funds(new_2, 200)
# print()
# new.transfer_funds(new_2, 100)

# Переказ коштів між рахунками
# print(new.transfer(new_2, 100))
# print(new.transfer(new_2, 100))
# print(new.transfer(new_2, 100))

# Зняття з разунку
# print(new.withdraw(100))
# print(new.withdraw(300))

