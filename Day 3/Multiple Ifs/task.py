print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter Your Age : "))
    if age <= 12:
        bill = 5
        print("You have to pay 5$")
    elif age <= 18:
        bill = 7
        print("You have to pay 7$")
    else:
        bill = 12
        print("You have to pay 12$")
    want_photo = input('Do you want to take a Photo, Type "y" for Yes and "n" for No')
    if want_photo == "y":
        bill+=3
    print(f"Your Final Bill is  ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
