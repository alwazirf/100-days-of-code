from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


profit = 0
is_on = True
menu = Menu()

order = CoffeeMaker()
money_machine = MoneyMachine()
while is_on:
    choice = input(f"What do you like? {menu.get_items()}: ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        order.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if order.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                order.make_coffee(drink)