# step 2 - generate random data
from art import vs, logo
import random
from data import data
import os

def get_random_account():
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"


# step 3 - check if the answer is right and give feedback to the user.


def check_answer(guess, a_follower_count, b_follower_count):
    """ Checks followers against user's guess and returns True if they got it right.
    Or False if they got it wrong."""
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'


# step 4 - move the B's position to A’s place if the answer is right
# step 5 repeat the process & keep counting the score.
score = 0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    print(logo)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"against B: {format_data(account_b)}")

    guess = input("who has more followers? type A or B: ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f'You are correct! Current_score: {score}')
    else:
        game_should_continue = False
        print("you are wrong! game over")