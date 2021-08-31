# Write your code here
import sqlite3
from random import randint


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS `card` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `number` TEXT,
        `pin` TEXT,
        `balance` INTEGER DEFAULT 0);''')
        self.conn.commit()

    def insert_card_data(self, number, pin):
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO `card` (`number`, `pin`)
        VALUES ('{}', '{}');'''.format(number, pin))
        self.conn.commit()

    def get_card_pin(self, card_number):
        cur = self.conn.cursor()
        cur.execute('''SELECT `pin`
        FROM `card`
        WHERE `number` = {};'''.format(card_number))
        pin_number = cur.fetchone()
        if pin_number is None:
            return None
        pin_number = str(pin_number[0])
        return pin_number

    def get_card_balance(self, card_number):
        cur = self.conn.cursor()
        cur.execute('''SELECT `balance`
        FROM `card`
        WHERE `number` = {};'''.format(card_number))
        balance = cur.fetchone()
        if balance is None:
            return None
        balance = balance[0]
        return balance

    def add_balance(self, card_number, add_balance):
        balance = self.get_card_balance(card_number)
        sum_balance = balance + add_balance
        cur = self.conn.cursor()
        cur.execute('''UPDATE `card`
        SET `balance` = {}
        WHERE `number` = {};'''.format(sum_balance, card_number))
        self.conn.commit()
        return sum_balance

    def check_account_existed(self, card_number):
        cur = self.conn.cursor()
        cur.execute('''SELECT "number"
        FROM `card`
        WHERE "number" = "{}";'''.format(card_number))
        queried_card_number = cur.fetchone()
        if queried_card_number is None:
            invalid_account = True
        else:
            invalid_account = False
        return invalid_account

    def extract_money(self, from_card_number, transfer_amount):
        cur = self.conn.cursor()
        cur.execute('''UPDATE `card`
        SET `balance` = `balance` - {}
        WHERE `number` = {};'''.format(transfer_amount, from_card_number))
        self.conn.commit()

    def transfer_money(self, to_card_number, transfer_amount):
        cur = self.conn.cursor()
        cur.execute('''UPDATE `card`
        SET `balance` = `balance` + {}
        WHERE `number` = {};'''.format(transfer_amount, to_card_number))
        self.conn.commit()

    def delete_account(self, card_number):
        cur = self.conn.cursor()
        cur.execute('''DELETE FROM `card`
        WHERE `number` = {}'''.format(card_number))
        self.conn.commit()


class Bank:
    def __init__(self):
        self.db = Database()
        self.account_identifier = None
        self.checksum = None
        self.card_number = None
        self.pin_number = None

    def create_account(self):
        major_industry_identifier = '400000'
        account_identifier = str(randint(0, 999_999_999))
        if len(account_identifier) < 9:
            account_identifier = '0' * (9 - len(account_identifier)) + account_identifier
        checksum = self.define_checksum(major_industry_identifier, account_identifier)
        self.card_number = major_industry_identifier + account_identifier + str(checksum)
        self.pin_number = str(randint(0, 9999))
        if len(self.pin_number) < 4:
            self.pin_number = '0' * (4 - len(self.pin_number)) + self.pin_number
        self.db.insert_card_data(self.card_number, self.pin_number)

    @staticmethod
    def define_checksum(major_industry_identifier, account_identifier):
        fifteen_digits = major_industry_identifier + account_identifier
        sum_15_digits = 0
        for index, digit in enumerate(fifteen_digits):
            digit = int(digit)
            if (index + 1) % 2 != 0:
                digit *= 2
            if digit > 9:
                digit -= 9
            sum_15_digits += digit
        checksum = 0
        if sum_15_digits % 10 != 0:
            checksum = 10 - (sum_15_digits % 10)
        return checksum

    def check_luhn_numbers(self, card_number):
        err_card_number = None
        checksum = self.define_checksum(card_number[:6], card_number[6:15])
        if checksum != int(card_number[-1]):
            err_card_number = True
        return err_card_number


class System:
    def __init__(self):
        self.db = Database()
        self.bank = Bank()
        self.is_exit = False

    def main_menu(self):
        while not self.is_exit:
            print('''1. Create an account\n2. Log into account\n0. Exit''')

            choice = int(input())

            if choice == 1:
                new_client = Bank()
                new_client.create_account()
                print(f'''Your card has been created
Your card number:\n{new_client.card_number}
Your card PIN:\n{new_client.pin_number}''')

            elif choice == 2:
                self.login_account()

            elif choice == 0:
                print('Bye!')
                self.is_exit = True

    def login_account(self):
        entered_card_number = input('Enter your card number:\n')
        entered_card_pin = input('Enter your PIN:\n')

        if entered_card_pin == self.db.get_card_pin(entered_card_number):
            print('You have successfully logged in!')
            self.login_menu(entered_card_number)

        else:
            print('Wrong card number or PIN!')
        pass

    def login_menu(self, entered_card_number):
        while True:
            print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
            logged_in_choice = int(input())

            if logged_in_choice == 1:
                balance = self.db.get_card_balance(entered_card_number)
                print(f"Balance: {balance}")

            if logged_in_choice == 2:
                income = int(input('Enter income:\n'))
                self.db.add_balance(entered_card_number, income)
                print('Income was added!')

            if logged_in_choice == 3:
                transfer_card_number = str(input('Transfer\nEnter card number:\n'))
                if transfer_card_number == entered_card_number:
                    print('You can\'t transfer money to the same account!')
                    continue

                invalid_card_number = self.bank.check_luhn_numbers(transfer_card_number)
                if invalid_card_number:
                    print('Probably you made a mistake in the card number. \nPlease try again!')
                    continue

                invalid_account = self.db.check_account_existed(transfer_card_number)
                if invalid_account:
                    print('Such a card does not exist.')
                    continue

                transfer_money = input('Enter how much money you want to transfer:\n')
                balance = self.db.get_card_balance(entered_card_number)
                if int(transfer_money) > int(balance):
                    print('Not enough money!')
                    continue

                self.db.extract_money(entered_card_number, transfer_money)
                self.db.transfer_money(transfer_card_number, transfer_money)
                print('Success!')

            if logged_in_choice == 4:
                self.db.delete_account(entered_card_number)
                print('The account has been closed!')

            if logged_in_choice == 5:
                print('You have successfully logged out!')
                break

            if logged_in_choice == 0:
                print('Bye!')
                self.is_exit = True
                break


if __name__ == '__main__':
    menu = System()
    menu.main_menu()
