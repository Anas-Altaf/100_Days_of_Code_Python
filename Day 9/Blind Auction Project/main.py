from art import logo

auction_data = {}
choice = True
print(logo)
while choice:
    name = input("Enter You Name : ")
    price =  round(float(input("Enter Your Bid Price : $")))
    auction_data[name] = price
    selection = input("For a new bidder type 'yes' otherwise 'no' : ").lower()
    print("\n"*30)
    if selection == 'yes':
        choice = True
    else:
        choice = False
        max_bid=0
        max_bidder_name=""
        for key in auction_data:
            if auction_data[key] > max_bid:
                max_bid = auction_data[key]
                max_bidder_name = key
        print(f"The winner is {max_bidder_name} with highest bid of ${max_bid}.")