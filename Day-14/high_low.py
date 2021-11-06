# logo and dependency
import game_data as gd
import random
import art
from replit import clear
## Use if statement to check if user is correct.
def checking_answer(guess, a_follower, b_follower):
    """Take the guess of the user and compare it with the actual answer"""
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess =='b'


# formating Data 
def format_account(account):    
    """Format the account data into printabe format"""
    account_name = account['name']
    account_followers = account['follower_count']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


is_game_over = True

print(art.logo)
data  = gd.data
score = 0
item_2 = random.choice(data)
# make the game repeatable.

while is_game_over:
    # Generate a random account from the game data.
    item_1 = item_2
    item_2 = random.choice(data)
    while item_2  == item_1:
        item_2 = random.choice(data)

    print(f"Compare A: {format_account(item_1)}")
    print(art.vs)
    print(f"Compare B: {format_account(item_2)}")

    # Ask user to guess 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Check if user is correct 
    ## Get followers count of Each account.
    a_follower_count = item_1['follower_count']
    b_follower_count = item_2['follower_count']
    clear()
    print(art.logo)
    
    ## Check if user is correct 
    is_correct =checking_answer(guess, a_follower_count, b_follower_count)

    # Give the user Feedback on their guess 
    if is_correct:
        score +=1
        print(f"You're right!, your score {score}")
    else:
        is_game_over = False
        print(f"Sorry you are Wrong!, your score {score}")




    # Making account repostionable 


# clear the screen between round 
