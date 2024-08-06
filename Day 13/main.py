# Debugging

# from random import randint

# dice_images = ["satu", "dua", "tiga", "empat", "lima", "enam"]
# dice_num = randint(0,5)

# print(dice_images[dice_num])
# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("Input pake angka !!!")
#     age = int(input("How old are you? "))

# if age > 10:
#     print(f"Bukan bocah {age}")


# debug again
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
import random

def add(a,b):
    return a+b

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item*2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
    b_list.append(new_item)
    print(b_list)
    
mutate([1,2,3,4,5,6])