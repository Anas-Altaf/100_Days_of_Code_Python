print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese =  input("Do you want extra cheese? Y or N: ").upper()
bill = 0
if size == "M":
    bill = 20
    if pepperoni == "Y":
        bill+=3
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill+=3
else:
    bill = 15
    if pepperoni == "Y":
        bill+=3
if extra_cheese == "Y":
    bill+=1
print(f"Your final bill is: ${bill}.")
