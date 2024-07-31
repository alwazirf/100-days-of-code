print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
ans1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if ans1 == "left":
    ans2 = input("You come to lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
    if ans2 == "wait":
        ans3 = input("You arrive at the island unharmed. There is a house with 3 door. One re, one yellow and one blue. Which color do you choose?\n")
        if ans3 == "blue":
            print("Eaten by beast.\nGame Over")
        elif ans3 == "red":
            print("Burned by fire")
        elif ans3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout\nGame Over")
else:
    print("Fall into a hole\nGame Over")
