import random
from urllib.parse import uses_relative

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
game_elements = [rock,paper,scissors]
user_choice = int(input("Choose one, Type 0 for Rock  | 1 for Paper | 2 for Scissors"))
system_choice=random.randint(0,2)
if 0<= user_choice <=3:
    print(f"\n{game_elements[user_choice]}\n")
    print(f"Computer Choice:\n{game_elements[system_choice]}\n")
    if user_choice == 0 and system_choice == 2:
        print("You Won!")
    elif user_choice == 1 and system_choice == 0:
        print("You Won!")
    elif user_choice == 2 and system_choice == 1:
        print("You Won!")
    elif user_choice == system_choice:
        print("Its Draw!")
    else:
        print("You Lose!")
else:
    print("Invalid Choice, You Lose!")
