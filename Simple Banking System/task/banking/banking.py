# Write your code here
from random import randint

cards = {}


class Bank:
    def __init__(self):
        self.account_identifier = None
        self.checksum = None
        self.card_number = None
        self.pin_number = None
        self.balance = 0

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
        cards[self.card_number] = {
            'pin_number': self.pin_number,
            'balance': self.balance
        }

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

    @staticmethod
    def check_balance(card_number):
        balance = cards[card_number]['balance']
        return balance


class System:
    def __init__(self):
        self.is_exit = False

    def main_menu(self):
        while not self.is_exit:
            print('''1. Create an account\n2. Log into account\n0. Exit''')

            choice = int(input())

            if choice == 1:
                new_client = Bank()
                new_client.create_account()
                print(f'''Your card has been created
Your card number:\n{new_client.card_number}\nYour card PIN:\n{new_client.pin_number}''')

            elif choice == 2:
                self.login_account()

            elif choice == 0:
                print('Bye!')
                self.is_exit = True

    def login_account(self):
        entered_card_number = input('Enter your card number:\n')
        entered_card_pin = input('Enter your PIN:\n')

        if entered_card_number in cards.keys() and cards[entered_card_number]['pin_number'] == entered_card_pin:
            print('You have successfully logged in!')
            self.login_menu(entered_card_number)

        else:
            print('Wrong card number or PIN!')
        pass

    def login_menu(self, entered_card_number):
        bank = Bank()
        while True:
            print('''1. Balance\n2. Log out\n0. Exit''')
            logged_in_choice = int(input())

            if logged_in_choice == 1:
                balance = bank.check_balance(entered_card_number)
                print(f"Balance: {balance}")

            if logged_in_choice == 2:
                print('You have successfully logged out!')
                break

            if logged_in_choice == 0:
                print('Bye!')
                self.is_exit = True
                break


if __name__ == '__main__':
    menu = System()
    menu.main_menu()
