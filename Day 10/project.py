def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

first_num = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operand  = input("Pick an operation: ")
second_num = int(input("What's the second number? "))
total = 0
continue_calc = True

    
while continue_calc:
    calculation_function = operations[operand]
    total = calculation_function(first_num, second_num)

    print(f"{first_num} {operand} {second_num} = {total}")
    
    ask_continue = input(f"Do you want to continue calculating with {total}? Type 'y' or 'n': ")
    if ask_continue == "n":
        continue_calc = False
    else:
        first_num = total
        operand = input("Pick an operation: ")
        second_num = int(input("What's the second number? "))