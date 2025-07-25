#Python Random Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running =True

print("Welcome to Python Number Guessing Game!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f" Please select a number between {lowest_num} and {highest_num}")

        elif guess>answer:
            print("That number is too high")
        elif guess<answer:
            print("That number is too low")
        else:
            print(f"The correct number is {answer}!")

    else:
        print("Please enter a valid number")
        print(f"Select a number between {lowest_num} and {highest_num}")
