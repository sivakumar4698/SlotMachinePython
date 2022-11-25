import random

MAXIMUM_LINE = 3
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


def depositamount():
    ## While True runs until a break statement gets executed inside the loop
    while True:
        deposit = input("enter the deposit amount to get started: $")

        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Amount should be greater than zero")
        else:
            print("Please enter a valid amount")
    
    return deposit

def get_slot_machine_spin(rows, cols, symbols):

    #Bringing all the symbols into a list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    print(all_symbols)

    #taking the allsymbols in the list and adding them randomly to each column. [[],[],[]]
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    print(columns)
    return columns


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        #taking the first value in each line
        symbol = columns[0][line]
        for column in columns:
            #comparing the first value with all the values in the line
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            #if all the values are same you win
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines   


def print_slot_machine(columns):
    # Print the columns inside the list as a slot machine view
    print(len(columns[0]))
    #taking the length of each column
    for row in range(len(columns[0])):
        #taking the index as well as the value
        for i, column in enumerate(columns):
            #printing the columns to look like a slot machine
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def get_bet_amount():
    while True:
        bet_amount = input("How much would like to bet on each line? $")

        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"The bet amount should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid amount")
    
    return bet_amount
    

def get_the_betting_lines():
    while True:
        no_of_lines = input("enter the number of lines to bet on (1 -" + str(MAXIMUM_LINE) + ")? ") 

        if no_of_lines.isdigit():
            no_of_lines = int(no_of_lines)
            if  1 <= no_of_lines <= MAXIMUM_LINE:
                break
            else:
                print("Enter a valid number of lines to bet on")
        else:
            print("Please enter a valid number")
    
    return no_of_lines


def spin(balance):
    lines = get_the_betting_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = depositamount()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()