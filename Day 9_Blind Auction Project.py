
from art import logo




bids = {}
bidding = True
while bidding:
    print(logo)
    your_name = input("what is your name?: ")
    your_bid = float(input("what is your bid?:"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bids[your_name] = your_bid
    print(bids)
    if other_bidders == "yes":
        print("\n" *20)
    if other_bidders == "no":
        bidding = False


highest_bidder = max(bids, key=bids.get) #get the max of which key
highest_bid = bids[highest_bidder]

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")