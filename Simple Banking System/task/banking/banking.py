# Write your code here
from random import seed
from random import randint
import sqlite3


# Create connection to database "card.s3db"
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# Create table "card" - DONE
# cur.execute("CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
# conn.commit()

# Set initial values
flag = True
new_card = ""
new_pin = ""


def menu1():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def generate_new_card():
    new_aid = ""
    inn = "400000"  # First 6 digits are fixed, INN = 400000

    seed()

    for i in range(1, 10):  # AID is 9 random digits
        new_aid = new_aid + str(randint(0, 9))

    aux_card = inn + new_aid  # Join INN and AID, pre Luhn algorithm
    checksum = luhn_algorithm(aux_card)  # Checksum is 1-digit long
    aux_card = aux_card + str(checksum)  # Add checksum

    return aux_card


def luhn_algorithm(i_card):
    card_list = []
    control_number = int(0)

    for x in range(15):  # Copy card string digits from i-card to card_list
        card_list.append(int(i_card[x]))

    for y in range(1, 16):  # Multiply odd digits by 2
        if y % 2 == 0:
            pass
        else:
            card_list[y-1] = card_list[y-1] * 2

    for z in range(1, 16):  # Subtract 9 to numbers over 9 & add latest digit
        if card_list[z-1] > 9:
            card_list[z-1] = card_list[z-1] - 9

        control_number = control_number + card_list[z-1]

    if control_number % 10 == 0:
        check_digit = 0
    else:
        check_digit = 10 - (control_number % 10)

    return check_digit


def generate_pin():
    aux = ""

    seed()

    for i in range(1, 5):  # PIN is 4 random digits
        aux = aux + str(randint(0, 9))

    return aux


def print_card_pin(i_card, i_pin):
    print("")
    print("Your card has been created")
    print("Your card number:")
    print(i_card)
    print("Your card PIN:")
    print(i_pin)
    print("")


def successful_login_message():
    print("")
    print("You have successfully logged in!")
    print("")


def failed_login_message():
    print("")
    print("Wrong card number or PIN!")
    print("")


def menu2():
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")


# Capture card and pin from user
def login_pair():
    print("")
    print("Enter your card number:")
    input_card = str(input())
    print("Enter your PIN:")
    input_pin = str(input())

    pair = [input_card, input_pin]

    return pair


# Tuple
# row[0]: id
# row[1]: number
# row[2]: pin
# row[3]: balance


# Determine number of rows on table "card"
def number_rows():
    cur.execute("SELECT * FROM card")
    rows = cur.fetchall()

    return len(rows)


# Retrieve full matching row
def matching_row(row):
    aux = [row[0]]
    cur.execute("SELECT * FROM card WHERE id = ?", aux)
    aux = cur.fetchone()

    return aux


# Print account balance
def menu2_1_balance(row):
    aux = matching_row(row)
    print("")
    print("Balance: " + str(aux[3]))
    print("")


# Deposit money into account
def menu2_2_income(row):
    print("")
    print("Enter income: ")
    income = int(input())

    aux = matching_row(row)

    # Arrange string for UPDATE statement
    new_balance = income + int(aux[3])
    aux = [new_balance, row[1]]

    update_balance(aux)

    print("Income was added!")
    print("")


def update_balance(balance_and_number):
    cur.execute("UPDATE card SET balance = (?) WHERE number = (?)", balance_and_number)
    conn.commit()


def menu2_3_transfer(origin_row):
    print("Transfer")
    print("Enter card number:")
    destination_number = str(input())

    # Prepare destination_number for Luhn algorithm check
    pre_luhn_number = ""

    # Copy first 15 digits to pre_luhn_card
    for i in range(15):
        pre_luhn_number = pre_luhn_number + destination_number[i]

    # Produce checksum against pre_luhn_card
    checked_digit = luhn_algorithm(pre_luhn_number)

    # Check destination number checksum is Luhn correct
    if checked_digit == int(destination_number[15]):
        # Refresh origin row
        origin_row = matching_row(origin_row)

        # Pull destination row
        destination_row = check_destination_card(destination_number)

        # Check destination number exist in table "card"
        if destination_row:
            # Check destination and origin numbers are the same
            if destination_row[1] == origin_row[1]:
                print("You can't transfer money to the same account!")
                print("")
            else:
                # Ask for how much money to transfer
                print("Enter how much money you want to transfer:")
                money_transfer = int(input())

                # Check origin balance has enough money to transfer
                if origin_row[3] < money_transfer:
                    print("Not enough money!")
                    print("")
                else:
                    # Transfer money
                    # Subtract money_transfer from origin balance
                    new_origin_balance = int(origin_row[3] - money_transfer)
                    aux = [new_origin_balance, origin_row[1]]
                    update_balance(aux)

                    # Add money_transfer to destination balance
                    new_destination_balance = int(destination_row[3] + money_transfer)
                    aux = [new_destination_balance, destination_row[1]]
                    update_balance(aux)

                    print("Success!")
                    print("")
        else:
            print("Such a card does not exist.")
            print("")
    else:
        print("Probably you made a mistake in the card number.")
        print("Please try again!")
        print("")


def check_destination_card(card):
    aux = [card]

    cur.execute("SELECT * FROM card WHERE number = ?", aux)
    aux = cur.fetchone()

    return aux


def menu2_4_close(row):
    aux = [row[1]]

    cur.execute("DELETE FROM card WHERE number = ?", aux)
    conn.commit()

    print("The account has been closed!")
    print("")


def successful_logout_message():
    print("You have successfully logged out!")
    print("")


def exit_message():
    print("")
    print("Bye!")
    print("")


while flag:
    menu1()
    menu1_option = int(input())

    if menu1_option == 1:
        new_card = generate_new_card()
        new_pin = generate_pin()

        next_id = number_rows() + 1
        new_row = [next_id, new_card, new_pin]

        # Insert new_row into table "card"
        cur.execute("INSERT INTO card (id, number, pin) VALUES (?, ?, ?)", new_row)
        conn.commit()

        print_card_pin(new_row[1], new_row[2])

    elif menu1_option == 2:
        card_pair = login_pair()

        cur.execute("SELECT * FROM card WHERE (number = ?) AND (pin = ?)", card_pair)
        match = cur.fetchone()

        if match:
            successful_login_message()

            while True:
                menu2()
                menu = int(input())

                if menu == 1:
                    menu2_1_balance(match)
                elif menu == 2:
                    menu2_2_income(match)
                elif menu == 3:
                    menu2_3_transfer(match)
                elif menu == 4:
                    menu2_4_close(match)
                    break
                elif menu == 5:
                    successful_logout_message()
                    break
                elif menu == 0:
                    flag = False
                    break
                else:
                    pass

        else:
            failed_login_message()

    elif menu1_option == 0:
        break

    else:
        pass

# cur.execute("DROP TABLE card")
# conn.commit()
# cur.execute("SELECT * FROM card")
# table_rows = cur.fetchall()
# print("")
# print("Total rows = ", len(table_rows))
# print(table_rows)

cur.close()
exit_message()
