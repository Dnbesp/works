# Банківський рахунок                   Беспятий Дмитро

class BankAccount:
    account_number = 0
    balance = 100

    def __init__(self, account_number, balance, owner_name):
        self.__account_number = account_number
        self._balance = balance
        self._balance += self._balance
        self.owner_name = owner_name

    def __str__(self):
         return f'account_number = {self.account_number}, balance = {self.balance}'

    # Поповнення рахунку
    def deposit(self, balance):
        self.balance += balance
        return f'Баланс поповнено! balance = {self.balance}'

    # Зняття з рахунку
    def withdraw(self, balance_draw):
        self.balance_draw = balance_draw
        if self.balance > 0:
            if self.balance - self.balance_draw < 0:
                return f"Помилка, у вас недостатньо коштів! Баланс = {self.balance}"
            else:
                self.balance = self.balance - self.balance_draw
                return f'З балансу знято {self.balance_draw}, Баланс = {self.balance}'
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
            print(f'Номер рахунку отримувача = {self.account_number}, balance = {self.balance}')
            print(f'Номер рахунку відправника = {self.obj.account_number}, balance = {self.obj.balance}')
            print("-" * 45)
            if self.value < 0:
                raise
            else:
                if self.obj.balance >= self.value:
                    self.obj.balance = self.obj.balance - self.value
                    self.balance = self.balance + self.value
                    resalt = "Переказ успішний"
                else:
                    resalt = "Значення переказу більше за баланс відправника"
        except RuntimeError:
            resalt = "Значення переказу повинно бути бельше за 0"
        finally:
            print(f'Номер рахунку отримувача = {self.account_number}, balance = {self.balance}')
            print(f'Номер рахунку відправника = {self.obj.account_number}, balance = {self.obj.balance}')
            print("-" * 45)

        return resalt

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

    # setter
    @account_number.setter
    def account_number(self, account_number):
        # print(self.__account_number)
        self.__account_number = account_number
        # print(self.__account_number)


Dm = BankAccount(12567, 2100, 'Dmytro')
N = BankAccount(13245, 5000, 'Nats')


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


