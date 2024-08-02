import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

charNull = []
for _ in range (len(chosen_word)):
    charNull += "_"
    
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        
        if letter == guess:
            charNull[i] = letter
            
    if guess not in chosen_word:
        lives -= 1
            
    print(charNull)
    
    if lives < 0:
        end_of_game = True
        print("You lose")
    
    if "_" not in charNull:
        end_of_game = True
        print("You win")