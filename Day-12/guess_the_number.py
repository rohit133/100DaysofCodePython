from typing import Tuple
from art import logo
import random
print(logo)

def guessing_parameter(number):
    """Check's the number is high or low depending on the Answer"""
    if number > random_num:
        return "Too High\nguess again"
    elif number < random_num:
        return "Too low\nguess again"
    

def easy_mode():
    """Allow the user to play in easy mode by giving 10 lives"""
    is_game_over = False
    game_live = 10
    print("You have 10 attempts to guess the number")
    while not is_game_over:
        guess = int(input("Make a guess: "))
        if guess == random_num:
            is_game_over = True
            game_live -=1
            print(f"You got it! The answer was {guess}")
        else:
            game_live -= 1
            if game_live == 0:
                print(f"You have {game_live} attempts to guess the number")
                print("You've run out of guesses, you lose.")
                is_game_over = True
            else:
                print(guessing_parameter(guess))
                print(f"You have {game_live} attempts left to guess the number")


def hard_mode():
    """Allow the user to play in hard mode by giving 5 lives"""

    is_game_over = False
    game_live = 5
    print("You have 5 attempts to guess the number")
    while not is_game_over:
        guess = int(input("Make a guess: "))
        if guess == random_num:
            is_game_over = True
            game_live -=1
            print(f"You got it! The answer was {guess}")
        else:
            game_live -= 1
            if game_live == 0:
                print(f"You have {game_live} attempts to guess the number")
                print("You've run out of guesses, you lose.")
                is_game_over = True
            else:
                print(guessing_parameter(guess))
                print(f"You have {game_live} attempts left to guess the number")
    

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_num = random.randint(1,101)
print(f" Testing Mode Your Answer is : {random_num}")

difficulty  = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    # CALL EASY GAME 
    easy_mode()

elif difficulty == 'hard':
    # CALL HARD GAME
    hard_mode()
