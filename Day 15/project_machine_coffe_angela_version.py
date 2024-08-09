from menu import MENU, resources, profit

def is_resource_sufficient(order_ingredient):
    """Return True if resource inggredients > order ingredient """
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return True if transaction successfull"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round((money_received - drink_cost), 2)
        print(f"Here is your change: {change}")
        return True
    else:
        print("Sorry. That was not enough. Money Refunded")
        return False

def process_coins():
    """"Return total calculated from coins inserted"""
    total = 0
    print("Please enter coins")
    total += int(input("How many quarter: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    
    return total

def make_coffe(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}. Enjoy!")

profit = 0
is_on = True
while is_on:
    choice = input("What do you like? Espresso, Latte or Cappuccino: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffe']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
