import unittest
from unittest import TestCase
from fifty_two import BankAccount
import requests
import json


class MainTest(TestCase):

    def setUp(self):
        BankAccount.accounts = []
        self.obj_BankAccount_1 = BankAccount(98765, 100, "Tanya", 'USD')
        self.obj_BankAccount_2 = BankAccount(55555, 300, "Ivan", 'EUR')
        BankAccount.create_exchange_rate()
        print('******')

    def tearDown(self):
        del self.obj_BankAccount_1
        del self.obj_BankAccount_2

    def test_create_obj_BankAccount(self):
        self.assertEquals(self.obj_BankAccount_1.account_number, 98765)
        self.assertEquals(self.obj_BankAccount_1.owner_name, "Tanya")
        self.assertEquals(self.obj_BankAccount_1.balance.amount, 100)
        self.assertEquals(self.obj_BankAccount_1.balance.currency, "USD")


    # Поповнення рахунку
    def test_deposit(self):
        self.assertEqual(self.obj_BankAccount_1.deposit(50), 'Баланс поповнено! balance = 150 USD')

    # Зняття з рахунку
    def test_withdraw(self):
        self.assertEquals(self.obj_BankAccount_1.withdraw(200), 'Помилка, у вас недостатньо коштів! Баланс = 100 USD')

    # Зміна імені власника рахунку
    def test_change_owner_name(self):
        self.assertEquals(self.obj_BankAccount_1.change_owner_name('Dima'), "Нове ім'я власника рахунку: Dima")

    # Вивід повної інформації про рахунок
    def test_display_account_info(self):
        self.assertEquals(self.obj_BankAccount_1.display_account_info(), "Номер рахунку: 98765, Баланс = 100 USD, "
                                                                         "Ім'я власника рахунку: Tanya")

    # Переказ коштів між рахунками
    def test_transfer(self):
        self.assertEquals(self.obj_BankAccount_1.transfer(self.obj_BankAccount_2, 100), "Переказ не можливий, "
                                                                                        "різні валюти")
    #
    # трансфер у випадку різних валют
    def test_transfer_funds(self):
        self.assertEquals(self.obj_BankAccount_1.transfer_funds(self.obj_BankAccount_2, 100), "Операція успішна")

    # перевірка рахунку на валідність
    def test_check_account_number(self):
        self.assertEquals(self.obj_BankAccount_1.check_account_number(98765), "Номер рахунку є валідним")

    # Знайти акаунт за Ім'ям
    def test_find_accounts_by_owner(self):
        self.assertEquals(self.obj_BankAccount_1.find_accounts_by_owner("Tanya"), ["Tanya"])

    # Порахувати середнье значення балансу для всіх акаунтів
    def test_get_average_balance(self):
        self.assertEquals(self.obj_BankAccount_1.get_average_balance(), 200)


if __name__ == '__main__':
    unittest.main()