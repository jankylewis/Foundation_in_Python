# original video: https://www.youtube.com/watch?v=th4OBktqK1I

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# check if all characters in a line are resembled
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # looping in every row
    for line in range(lines):
        # we then say all the symbols at the current row have to resemble the first column
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # multiplier of symbol: 5, 4, 3, 2
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .items means giving you a key and a value associated with dictionary
    # symbol plays as key
    # symbol_count plays as value
    for symbol, symbol_count in symbols.items():
        # _ means anonymous variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # this list will contain several list inside it -> nested lists (contain the list below: column [] after each iteration)
    columns = []
    # for every column we need to generate a certain number of symbols
    for _ in range(cols):
        column = []
        # : sign to copy the all_symbols list
        # anything happened with current_symbols will affect all_symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    # this assumes that there will be at least 1 item -> if no items presenting there -< will be crashed
    for row in range(len(columns[0])):
        # enumerate gives us the index of columns list
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a positive number!")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines between 1 and {str(MAX_LINES)}!")
        else:
            print("Please enter a positive number!")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}!")
        else:
            print("Please enter a positive number!")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    # while loop handles running game
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to spin (q to quit the game).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


try:
    main()
except:
    print(Exception("\nThere was an exception that interrupted the program."))
