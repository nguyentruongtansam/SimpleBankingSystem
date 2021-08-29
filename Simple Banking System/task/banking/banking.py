# Write your code here
from random import randint

cards = {}


class Client:
    def __init__(self):
        self.account_identifier = None
        self.checksum = None
        self.card_number = None
        self.pin_number = None
        self.balance = 0

    def create_account(self):
        self.account_identifier = str(randint(0, 999_999_999))
        self.checksum = str(randint(1, 9))
        if len(self.account_identifier) <9:
            self.account_identifier = '0' * (4 - len(self.account_identifier)) + self.account_identifier
        self.card_number = '400000' + self.account_identifier + self.checksum
        self.pin_number = str(randint(0, 9999))
        if len(self.pin_number) < 4:
            self.pin_number = '0' * (4 - len(self.pin_number)) + self.pin_number
        cards[self.card_number] = {
            'pin_number': self.pin_number,
            'balance': self.balance
        }


logging = True
while logging:

    print('''1. Create an account\n2. Log into account\n0. Exit''')

    choice = int(input())

    if choice == 1:
        new_client = Client()
        new_client.create_account()
        print(f'''Your card has been created\nYour card number:\n{new_client.card_number}\nYour card PIN:\n{new_client.pin_number}''')

    elif choice == 2:
        entered_card_number = input('Enter your card number:\n')
        entered_card_pin = input('Enter your PIN:\n')

        if entered_card_number in cards.keys() and cards[entered_card_number]['pin_number'] == entered_card_pin:
            print('You have successfully logged in!')
            logged = True
            while logged:
                print('''1. Balance\n2. Log out\n0. Exit''')
                logged_in_choice = int(input())

                if logged_in_choice == 1:
                    print(f"Balance: {cards[entered_card_number]['balance']}")
                    pass

                if logged_in_choice == 2:
                    print('You have successfully logged out!')
                    logged = False

                if logged_in_choice == 0:
                    print('Bye!')
                    logged = False
                    logging = False

        else:
            print('Wrong card number or PIN!')

        continue

    elif choice == 0:
        print('Bye!')
        logging = False
