import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Define a constant for the separator
SEPARATOR = "====================================="

want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

user_cards = []
com_cards = []

def sum_card(cards):
    total = 0
    for card in cards:
        total += card
    return total

def pick_card(card_before):
    card_before.append(random.choice(cards))
    
def output_score(u_card, c_card):
    print(f"Your cards: {user_cards}, current score: {sum_card(u_card)}")
    print(f"Computer first card: {c_card}")

def blackjack_game():
    for _ in range(0,2):
        user_cards.append(random.choice(cards))
    com_cards.append(random.choice(cards))

    user_total = sum_card(user_cards)
    com_total = sum(com_cards)

    output_score(user_cards, com_cards)
    any_pick = True
    while any_pick:
        pick_any_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
        if pick_any_card == 'y':
            pick_card(user_cards)
            user_total = sum_card(user_cards)
            output_score(user_cards, com_cards)
            if (user_total > 21):
                print(SEPARATOR)
                print(f"    Your final hand= {user_cards}, final score: {user_total}")
                print(f"    Computer's final hand: {com_cards}, final score: {com_total}")
                print("You went over. You lose")
                any_pick = False
        else:
            while sum_card(com_cards) < 17:
                pick_card(com_cards)
            com_total = sum(com_cards)
            if user_total > com_total:
                print(SEPARATOR)
                print(f"    Your final hand= {user_cards}, final score: {user_total}")
                print(f"    Computer's final hand: {com_cards}, final score: {com_total}")
                print("You win!!!!")
            else:
                print(SEPARATOR)
                print(f"    Your final hand= {user_cards}, final score: {user_total}")
                print(f"    Computer's final hand: {com_cards}, final score: {com_total}")
                print("You lose!!!")
            any_pick = False

blackjack_game()