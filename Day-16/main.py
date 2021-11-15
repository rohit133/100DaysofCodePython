from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report()
menu = Menu()
Money_machine = MoneyMachine()
Coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    choice = input(f"what would like to have {menu.get_items()} :").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        Coffee_maker.report()
        Money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if Coffee_maker.is_resource_sufficient(drink) and  Money_machine.make_payment(drink.cost):
            Coffee_maker.make_coffee(drink) 


        

        