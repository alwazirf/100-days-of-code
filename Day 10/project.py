first_num = int(input("What's the first number? "))
print("+\n-\n*\n/")
operand  = input("Pick an operation: ")
second_num = int(input("What's the second number? "))
total = 0
continue_calc = True

def calculation(first_num, second_num, operand):
    if operand == "+":
        total = first_num + second_num
        return total
    elif operand == "-":
        total = total = first_num - second_num
        return total
    elif operand == "*":
        total = total = first_num * second_num
        return total
    elif operand == "/":
        total = first_num / second_num
        return total
    else:
        return "Invalid operation"
    
while continue_calc:
    total = calculation(first_num=first_num, second_num=second_num, operand=operand)
    print(f"{first_num} {operand} {second_num} = {total}")
    
    ask_continue = input(f"Do you want to continue calculating with {total}? Type 'y' or 'n': ")
    if ask_continue == "n":
        continue_calc = False
    else:
        first_num = total
        operand = input("Pick an operation: ")
        second_num = int(input("What's the second number? "))