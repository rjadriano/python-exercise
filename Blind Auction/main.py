import art
print(art.logo)

bidders = {}
bid_on_going = "yes"

while bid_on_going == "yes":
    name = input("What is your name?: ")
    bid_price = input("What is your bid?: $")
    bidders[name] = int(bid_price)

    bid_on_going = input("Are there any other bidders? Type yes or no.").lower()
    # clear screen
    print("\n" * 100)


winner_name = ''
for key in bidders:
    winner_name = key if winner_name == '' else winner_name
    if bidders[key] > bidders[winner_name]:
        winner_name = key

print(bidders)
print(f"The winner is {winner_name} with a bid of {bidders[winner_name]}")