from menu import MENU, resources
from money import COIN_VALUES, CURRENCY
from time import sleep


menu = MENU
money = 0
resources = resources
profit = 0
machine_on = True

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
    
def process_money():
    c_money = 0
    for coin in COIN_VALUES:
        c_money += int(input(f"How many {coin}? please: ")) * COIN_VALUES[coin]
    print(f'You have provided: {CURRENCY}{c_money}')
    return c_money

def make_money(cost):
    u_money = process_money()
    if u_money > cost:
        change = round((u_money - cost),2)
        print(f"Here is {CURRENCY}{change} in change.")
        u_money = 0
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        u_money = 0
        return False
    

def off_the_machine(time):
    global machine_on
    print("Machine was off!!!")
    machine_on = False
    sleep(time)

while machine_on:
    answer = input("Prompt user by asking “What would you like? (espresso/latte/cappuccino): ").lower()

    if answer == "report":
        make_report({money})
    elif answer == "off":
        off_the_machine(10)
    elif check_order(menu, answer) is None:
        print("Please choose an available option.!!!")
    else:
        drink = check_order(menu, answer)
        sufficient_resources = check_resource(resources, drink)
        service_coffe = make_money(menu[answer]["cost"])
        if service_coffe:
            money += menu[answer]["cost"]
        
        if sufficient_resources:
            print('Thank you! Allow us to make your beverage now...')
            make_coffe(resources, drink)
            sleep(3)