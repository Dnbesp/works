from name import NewBankAccount
import json
import requests


class UpBankAccount(NewBankAccount):

    """class UpBankAccount import from name.py -> class NewBankAccount"""

    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transaction):
        super().__init__(account_number, balance, owner_name, currency, max_limit, max_count_transaction)

    #3. Перевизначте магічний метод `__eq__`, результатом має бути `True`,
    # якщо валюти у об’єктів співпадають, а `False` - в іншому випадку.
    def __eq__(self, other):
        return self.balance.currency == other.balance.currency

    #4. Перевизначити методи __lt__, __le__, __gt__, __ge__, що дозволяють порівнювати рахунки за балансом.
    # У випадку, якщо валюти не збігаються у об’єктів, то здійснити конвертацію до гривні, щоб порівняти.
    # Наприклад, r1 < r2 значить, що баланс рахунку у екземпляра r1 менший, ніж баланс у екземпляра r2.
    def __lt__(self, other):
        if self.balance.currency == other.balance.currency:
            if self.balance.amount < other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'< рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            elif self.balance.amount > other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'> рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            else:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'= рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
        else:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            json_text = json.loads(response.text)
            for item in json_text:
                if item["cc"] == self.balance.currency:
                    hrn_money_1 = round(item['rate'] * self.balance.amount, 2)
                if item["cc"] == other.balance.currency:
                    hrn_money_2 = round(item['rate'] * other.balance.amount, 2)
            if hrn_money_1 < hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' < рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            elif hrn_money_1 > hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' > рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            else:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' = рахунока №2: {other.account_number}({hrn_money_2} грн.)')

    def __le__(self, other):
        if self.balance.currency == other.balance.currency:
            if self.balance.amount <= other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'<= рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            else:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'> рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
        else:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            json_text = json.loads(response.text)
            for item in json_text:
                if item["cc"] == self.balance.currency:
                    hrn_money_1 = round(item['rate'] * self.balance.amount, 2)
                if item["cc"] == other.balance.currency:
                    hrn_money_2 = round(item['rate'] * other.balance.amount, 2)
            if hrn_money_1 <= hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' <= рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            else:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' > рахунока №2: {other.account_number}({hrn_money_2} грн.)')

    def __gt__(self, other):
        if self.balance.currency == other.balance.currency:
            if self.balance.amount < other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'< рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            elif self.balance.amount > other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'> рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            else:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'= рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
        else:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            json_text = json.loads(response.text)
            for item in json_text:
                if item["cc"] == self.balance.currency:
                    hrn_money_1 = round(item['rate'] * self.balance.amount, 2)
                if item["cc"] == other.balance.currency:
                    hrn_money_2 = round(item['rate'] * other.balance.amount, 2)
            if hrn_money_1 < hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' < рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            elif hrn_money_1 > hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' > рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            else:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' = рахунока №2: {other.account_number}({hrn_money_2} грн.)')

    def __ge__(self, other):
        if self.balance.currency == other.balance.currency:
            if self.balance.amount >= other.balance.amount:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'>= рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
            else:
                print(f'рахунок №1: {self.account_number}({self.balance.amount} {self.balance.currency}) '
                      f'< рахунока №2: {other.account_number}({other.balance.amount} {other.balance.currency})')
        else:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            json_text = json.loads(response.text)
            for item in json_text:
                if item["cc"] == self.balance.currency:
                    hrn_money_1 = round(item['rate'] * self.balance.amount, 2)
                if item["cc"] == other.balance.currency:
                    hrn_money_2 = round(item['rate'] * other.balance.amount, 2)
            if hrn_money_1 >= hrn_money_2:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' >= рахунока №2: {other.account_number}({hrn_money_2} грн.)')
            else:
                print(f'рахунок №1: {self.account_number}({hrn_money_1} грн.)'
                      f' < рахунока №2: {other.account_number}({hrn_money_2} грн.)')

    # 5. Перевизначити __bool__: метод дозволяє перевірити, чи є екземпляр класу UpBankAccount «істинним»
    # (True, якщо баланс додатній) або «хибним» (False, в іншому випадку).
    def __bool__(self):
        if self.balance.amount > 0:
            return True
        else:
            return False

    # 6. Реалізуйте операції: додавання __add__ екземпляра r і деякого додатного числа numb (r + numb),
    # яка буде відповідати поповненню рахунку r на це число та повернення того самого екземпляра (id однакове).
    # Аналогічно реалізуйте віднімання r - numb, що відповідає за зняття коштів.
    def __add__(self, other):
        self.balance.amount += other
        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file5:
            text = file5.readline()
            text = "account_number balance currency owner_name" + '\n'
            file5.seek(0)
            file5.writelines(text)
            file5.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

        print(f'Баланс рахунку {self.account_number} поповнено. Рахунок складає {self.balance}')

    def __sub__(self, other):
        if self.balance.amount >= other:
            self.balance.amount -= other
            with open(f'data/account_number_{self.account_number}.txt', 'r+') as file5:
                text = file5.readline()
                text = "account_number balance currency owner_name" + '\n'
                file5.seek(0)
                file5.writelines(text)
                file5.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')
            print(f'З рахунку {self.account_number} знято {other} {self.balance.currency}. '
                  f'Рахунок складає {self.balance}')
        else:
            print(f'Баланс менше суми для зняття.')

    # 7. Перевизначити метод `__call__(self, value=0)`, щоб при виклику на об'єкті друкувалось повідомлення про зміну
    # балансу об’єкта і якщо value<0 -здійснюється зняття коштів у розмірі value, а при value>0 - поповнення рахунку,
    # при value=0 - просто виводимо стан рахунку. Наприклад, маємо екземпляр r нашого класу. Тоді, r(-10) знімає з
    # рахунку кошти у розмірі 10, а r(10) - робить поповнення, інакше, якщо r() або r(0) - друкуємо стан рахунку.
    def __call__(self, value=0):
        if value < 0:
            self.balance.amount -= (-value)
            print(f"з рахунку {self.account_number} знято {value}")
        elif value > 0:
            self.balance.amount += value
            print(f'рахунок {self.account_number} поповнено на {value}')
        else:
            print(f'на рахунку {self.account_number}, баланс становить {self.balance}')
        with open(f'data/account_number_{self.account_number}.txt', 'r+') as file5:
            text = file5.readline()
            text = "account_number balance currency owner_name" + '\n'
            file5.seek(0)
            file5.writelines(text)
            file5.writelines(f'{str(self.account_number)} {str(self.balance)} {str(self.owner_name)} \n')

    # 8. Перевизначити метод __setattr__(self, name, value) так, щоб при спробі встановити значення value для атрибуту,
    # що відповідає за баланс, виводило повідомлення про “зміну балансу, скільки було ... і стало ...” і встановлювало
    # відповідне значення цього атрибуту за допомогою виклику object.__setattr__(self, name, value) або присвоєння
    # self.__dict__[name] = value. Це забезпечить нас “сигналами” про зміну балансу у об’єктів.


new = UpBankAccount(12567, 5100, 'Dmytro', "USD", 300, 2)
# new_2 = UpBankAccount(13456, 100, 'Ivan', "EUR", 700, 3)

#8

new.balance.amount = 5600
# new_2.balance.amount = 400

#7
# new(-100)
# new(+200)
# new(0)
#6
# new + 200
# new_2 - 100
#5
# print(bool(new))
# print(bool(new_2))
#4
# new < new_2
# new <= new_2
# new_2 > new
# new >= new_2
#3
# print(new == new_2)
