from art import logo
from replit import clear
print(logo)
auction = {} 
flag = False
winner = ""

def bidding_record (bidding_reco):
    high_bid = 0
    for bidder in bidding_reco:
        bid_amount = bidding_reco[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${high_bid}")


while not flag :
    name = input("what's your name? ")
    bid = int(input("Your bid: "))
    auction [name] = bid
    result = input("Anyother Bidder in the room?\n")
    if result == "no":
        flag = True
        clear()
        bidding_record(auction)
    elif result == "yes":
        clear()


