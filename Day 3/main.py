# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5;
#         print(f"Child tikets are {bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tikets are {bill}")
#     else:
#         bill = 12
#         print(f"Adult tikets are {bill}")
#     want_photo = input("Do you want a photo taken? Y or N? ")
#     if want_photo == "Y":
#         #add to bill
#         bill += 3
#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")


print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5;
        print(f"Child tikets are {bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tikets are {bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Wes tikets are {bill}")
    else:
        bill = 12
        print(f"Adult tikets are {bill}")
    want_photo = input("Do you want a photo taken? Y or N? ")
    if want_photo == "Y":
        #add to bill
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")