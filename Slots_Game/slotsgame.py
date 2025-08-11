#Python Slots Game
import random
from unittest import result


#In this game, we will accept a user input 'bet', which will be deducted from the current balance.
#If all 3 symbols match, you will win a certain amount of money, which will be added to your balance.

#Don't Gamble IRL!

def spin_row():
    symbols = ['@' ,'#', '$', '&']

    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print(' '.join(row))

def get_payout(row,bet):
    if row[0] == row[1] and row[2]:
        if row[0] == "@":
            return bet * 2
        elif row[0] == "#":
            return bet * 3
        elif row[0] == "$":
            return bet * 10
        elif row[0] == "&":
            return bet * 5
    return 0

def main():
    pass

balance = 100000
print("Welcome to The Slot Machine!")
print("Play Big, Win Big!")
print("The Symbols are: @ , # , $ , &")

while balance > 0:
    print(f"Your balance is ₹ {balance}")

    bet = input("Enter your bet: ")

    if not bet.isdigit():
        print("Please enter a valid number.")
        continue

    bet = int(bet)
    if bet <= 0:
        print("Bet must be greater than 0.")
        continue

    if bet > balance:
        print("You funds are insufficient.")
        continue

    balance -= bet

    row = spin_row()
    print("Spinning . . . \n")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
        print(f"You won ₹{payout}.")
    else:
        print("Sorry you lost this round")
        print("Better luck next time!")

    balance += payout

    play_again = input("Do you want to play again? (Y/N): ").upper()

    if play_again != "Y":
        print("Are you sure you don't want to play again?")
        print("You can always win next time!")

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            print(f"Game Over! Your final balance is {balance}")
            print("Come back soon!")
            break


if __name__ == '__main__':
    main()
