MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check Resources is sufficient
def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Update the Resources ingredients for {items} is insufficient")
            return False
        return True

def print_report():
    """Create a report of the the Resources"""
    # Printing Report
    print("Report\n")
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${profit}")



# ask for the user for Coins and process it
def process_coin(): 
    """Returns the total calculated from coins inserted."""
    print("Insert Coins:\n")
    total = float(input("how many quarters: "))*0.25
    total += float(input("how many dimes: "))*0.10
    total += float(input("how many nickles: "))*0.05
    total += float(input("how many pennies: "))*0.01
    return total

def is_transactions_successful(amount_received,drink_cost):
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost,2)
        print(f"Here's your ${change} in change.")
        global profit 
        profit += drink_cost
        return True 
    else:
        print("Not enough money !")
        return False



def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name} ☕")
    

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print_report()
    else:
        drink =  MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coin()
            if is_transactions_successful(payment, drink['cost']):
                make_coffee(choice,drink['ingredients'])
            




