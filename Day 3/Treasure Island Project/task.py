print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
selection = input("Where do you wanna go? left | right\n").lower()
if selection == "left":
    print("You reached at the sea.")
    selection = input("You wanna 'swim'🏊‍♀️ or 'wait'🚤 for the boat? swim | wait\n").lower()
    if selection == "wait":
        selection = input("You have 3 doors in front of you\n Choose one door: red🔴 | yellow🟡 | blue🔵\n").lower()
        if selection == "yellow":
            print("Congrats!, You found the Treasure 🤑")
        elif selection == "red":
            print("You are burnt by the Fire🔥, Bye Bye!🏴‍☠️")
        elif selection == "blue":
            print("You are died by the ice storm🧊, Bye Bye!🏴‍☠️")
        else:
            print("You fell into a dark room, Be Here Always💀")
        print("Game Over!🔚")
    else:
        print("You are swallowed bt a Trout, Bye Bye!🏴‍☠️")

else:
    print("You fall into a hole, Bye Bye!🏴‍☠️")