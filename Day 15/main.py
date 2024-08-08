from menu import MENU, resources
from time import sleep

def check_resource(res, drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    can_make = True
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > res[item]:
            print(f"Sorry there is not enough {item}.")
            can_make = False
    return can_make

def check_order(menu, order_name):
    """Search the menu for a particular drink by name. return if exist"""
    for item in menu:
        if item == order_name:
            return menu[item]
    print(f"Sorry your {order_name} is not available")

def make_coffe(res, order):
    for item in order["ingredients"]:
        res[item] -= order["ingredients"][item]
    
def make_report(money):
    res = resources
    print(f"Water : {res["water"]}ml\n Milk : {res["milk"]}ml\n Coffe : {res["coffee"]}g\n Money : ${money}")
    
def off_the_machine(time):
    print("Machine was off!!!")
    sleep(time)

answer = input("Prompt user by asking “What would you like? (espresso/latte/cappuccino): ").lower()
menu = MENU
money = 0
resources = resources

if answer == "report":
    make_report({money})
elif answer == "off":
    off_the_machine(10)
elif check_order(menu, answer) is None:
    print("Please choose an available option.!!!")
else:
    drink = check_order(menu, answer)
    sufficient_resources = check_resource(resources, drink)
    
    if sufficient_resources:
        print('Thank you! Allow us to make your beverage now...')
        make_coffe(resources, drink)
        sleep(3)