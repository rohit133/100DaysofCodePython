from math import radians
import random
from replit import clear
from art import logo
# declaring Card Deck and random 
def deal_card():
    """Return a random card from the deck of card it uses the random.choice function to pick random number from the Sequence"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card  = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of card and return the scores after perfroming some calculations"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == calculate_score:
        print('Draw')
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over, You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. you win 😀"
    elif user_score > computer_score:
        return "You win 😎😎"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f" Your cards: {user_card} and your scores {user_score} ")
        print(f" Computer first card {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            if input("Do you want to deal the another card press 'y' and press 'n' to pass: ") == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True 


    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your final hand: {user_card}, Final scores {user_score} ")
    print(f" Computer final hand {computer_card}, Final Score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
    clear()
    play_game()
