
def auction():
    print("Welcome to our auction...")
    print("Who do we have here?")
    bidders = {}
    active = True

    while active:
        name = input("What is your name? ").title()
        bid_price = int(input("What is your bid price? $ "))
        
        if not bid_price in bidders.values():
            bidders[name] = bid_price
        else:
            print("Already given. Choose another price.")
        
        next_bidder = input("Are there any other bidders? (y,n) ").lower()
        
        if next_bidder == "y":
            print("\n\n\n\n\n\n\n\n")
            continue
        else:
            active = False

    highest = max(list(bidders.values()))
    winner = None

    for k,v in bidders.items():
        if v == highest:
            winner = k

    print(f"The winner with the highest bid is: {winner} with the bid of ${highest}")
    

auction()
    