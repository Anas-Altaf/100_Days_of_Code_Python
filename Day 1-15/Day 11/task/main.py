import random
from art import  logo
# --------- Functions
def clear_cards():
    user_cards.clear()
    c_cards.clear()
def calculate_score():
    return sum(user_cards), sum(c_cards)
def display_info():
    print(f"User Cards : {user_cards} |  User Score : {user_score}")
    print(f"Computer First Card : {c_cards[0]}  | c Score : {c_score}")
def init_cards():
    clear_cards()
    for i in range(2): # 2 Cards for User
        user_cards.append(random.choice(cards))
        c_cards.append(random.choice(cards))
def draw_user_card():
    user_cards.append(random.choice(cards))
    print("User Drawn a Card")
def draw_c_card():
    c_cards.append(random.choice(cards))
    print("c Drawn a card")
def user_wins():
    display_info()
    print("User Wins")
def c_wins():
    display_info()
    print("Computer Wins")
def drawn():
    display_info()
    print("Game Draw")

# ----------
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_playing = False
draw_cards = True
user_cards = []
c_cards = []
user_score = 0
c_score = 0
print(logo)
wanna_play = input("Do You wanna play the Blackjack ? 'y' or 'n' : ").lower()
if "y" in wanna_play:
    is_playing = True
else:
    is_playing = False
while is_playing:
    init_cards()
    user_score ,c_score  = calculate_score()
    display_info()
    while draw_cards and is_playing:
        user_score ,c_score  = calculate_score()
        if user_score == c_score == 21:
            drawn()
            is_playing = False
            draw_cards = False
        elif user_score == 21:
            user_wins()
            is_playing = False
            draw_cards = False
        elif c_score == 21:
            c_wins()
            is_playing=False
            draw_cards = False
        else:
            if user_score > 21:
                if 11 in user_cards:
                    print("User had an Ace")
                    user_cards[user_cards.index(11)] = 1
                    user_score ,c_score  = calculate_score()
                    # display_info()
                    if user_score > 21:
                        c_wins()
                        is_playing  = False
                        draw_cards = False
                else:
                    c_wins()
                    is_playing = False
                    draw_cards = False
            else:
                wanna_get_card = input("Do you want to get a card 'y' or stand 'n' : ").lower()
                if "y" in wanna_get_card:
                    draw_cards = True
                    draw_user_card()
                    user_score ,c_score  = calculate_score()
                    # display_info()
                else:
                    draw_cards = False
    if is_playing:
        while c_score < 17:
            draw_c_card()
            user_score ,c_score  = calculate_score()
            # display_info()
        if c_score > 21:
            user_wins()
            is_playing = False
        else:
            if user_score == c_score:
                drawn()
                is_playing = False
            elif user_score > c_score:
                user_wins()
                is_playing = False
            else:
                c_wins()
                is_playing = False
