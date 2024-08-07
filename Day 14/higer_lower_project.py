from art import vs, logo
from random import choice
from data import data
import os

#create function to get random choice for A and B

def choice_data():
    return choice(data)

def compare_follower(data_1, data_2, score):
    """This function to compare data"""
    if data_1['follower_count'] > data_2['follower_count']:
        score += 1
    return score

a_data = choice_data()
b_data = choice_data()
if a_data == b_data:
    b_data = choice_data()
game_should_continue = True

while game_should_continue:
    current_score = 0
    print(logo)
    if a_data == b_data:
        b_data = choice_data()
        
    print(f"Compare A: {a_data['name']}, {a_data['description']}, from {a_data['country']}")
    print(vs)
    print(f"Against B: {b_data['name']}, {b_data['description']}, from {b_data['country']}")
    print(current_score)

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if answer == 'a':
        if a_data['follower_count'] > b_data['follower_count']:
            current_score += 1
        else:
            current_score += 0
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_should_continue = False
    elif answer == 'b':
        if a_data['follower_count'] < b_data['follower_count']:
            current_score += 1
        else:
            current_score += 0
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_should_continue = False
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        game_should_continue = False

    a_data = b_data
    b_data = choice_data()
    # os.system('cls')

#Function to compare a and b

#function calculate score

#function game