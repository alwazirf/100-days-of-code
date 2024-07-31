import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)


comChose = random.randint(0,2)
print(f"Computer chose {comChose}")

if comChose == 0:
    print(rock)
elif comChose == 1:
    print(paper)
elif comChose == 2:
    print(scissors)

if choice == comChose:
    print("Draw!!!")
elif choice == 0 and comChose == 1:
    print("You lose!")
elif choice == 0 and comChose == 2:
    print("You win!")
elif choice == 1 and comChose == 0:
    print("You win!")
elif choice == 1 and comChose == 2:
    print("You lose!")
elif choice == 2 and comChose == 0:
    print("You lose!")
elif choice == 2 and comChose == 1:
    print("You win!")
else:
    print("You typed an invalid number, you lose!")