import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#eazy level
# password = ""
# for i in range(1, nr_letter+1):
#     password += random.choice(letters)
# for i in range(1, nr_symbols+1):
#     password += random.choice(symbols)
# for i in range(1, nr_numbers+1):
#     password += random.choice(numbers)
# print(password)


password = []
for i in range(1, nr_letter+1):
    password.append(random.choice(letters))
for i in range(1, nr_symbols+1):
    password.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
    password.append(random.choice(numbers))
random.shuffle(password)

newPassword = ""
for i in password:
    newPassword += i
print(newPassword)