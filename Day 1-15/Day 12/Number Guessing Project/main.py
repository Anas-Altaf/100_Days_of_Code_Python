import random

from art import logo

def guess_number(random_guess:int, num_of_tries:int):
    while True:
        if num_of_tries < 1:
            print("You have ran out of Tries")
            return
        else:
            print(f"Remaining Tries : {num_of_tries}")
            user_guess = int(input("Guess the number : "))
            if user_guess == random_guess:
                print("Yeah! 🤗, You guess it correctly!")
                return
            elif  user_guess > random_guess:
                print("Too High!")
            else:
                print("Too Low!")
        num_of_tries-=1
def game():
    total_tries = 10
    min_limit = 1
    max_limit = 100
    random_guessed = random.randint(1,100)
    # Main
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_limit} and {max_limit}.")
    mode = input("Type the mode you want to play , 'easy' | 'hard' >: ")
    if mode == "easy":
        total_tries =10
    else:
        total_tries =5
    print(f"You have total {total_tries} tries.")
    guess_number(random_guessed, total_tries)

game()