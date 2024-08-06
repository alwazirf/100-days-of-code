import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice == 'easy':
    total_attempts = 10
elif choice == 'hard':
    total_attempts = 5
else:
    print("Wrong Choice. Thankyou")
    
number = random.randint(1,100)

    
def decrease_attempts(attempt):
    attempt -= 1
    return attempt
    
def number_guessing():
    global total_attempts
    while total_attempts > 0:
        print(f"You have {total_attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == number:
            print("You win")
            return
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print("error some of data.")
        
        total_attempts = decrease_attempts(total_attempts)
        if total_attempts != 0:
            print("Guess again.")
    
    if total_attempts == 0:
        print("You've run out of guesses, you lose.")
        
number_guessing()