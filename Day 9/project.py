from art import logo

print(logo)

print("Welcome to the secret auction program")

bids = {}
end_of_auction = False

def find_higest_bidder(binding_record):
    higest_bind = 0
    winner = ""
    for binder in binding_record:
        if binding_record[binder] > higest_bind:
            higest_bind = binding_record[binder]
            winner = binder
    print(f"The winner is {winner} with a bid of ${higest_bind}")


while not end_of_auction:
    name = input("What is your name?: ")
    bind = int(input("What's your bind?: $"))
    bids[name] = bind
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        end_of_auction = True
        find_higest_bidder(bids)
