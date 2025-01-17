import random
from game_data import data as entities_data_set
from art import logo, vs


def get_random_entity(data_set):
    """
    Takes data_set_list as input
    :return: random dict of data_set
    """
    return random.choice(data_set)


def get_entity_name(e: dict):
    return e["name"]


def get_entity_country(e: dict):
    return e["country"]


def get_entity_desc(e: dict):
    return e["description"]


def get_entity_follower_count(e: dict):
    return e["follower_count"]


def view_entity(e: dict):
    name = e['name']
    country = e["country"]
    follower_c = e["follower_count"]
    desc = e["description"]
    return f"{name} is a {desc}, from {country}"


def compare_entities_follower_count(greater_e: dict, lesser_e: dict):
    return get_entity_follower_count(greater_e) > get_entity_follower_count(lesser_e)


def are_entities_same(e_a, e_b):
    return e_a == e_b


def game():
    entity_a = get_random_entity(entities_data_set)
    answer_is_correct = True
    score = 0
    print(logo)
    while answer_is_correct:
        print(
            fr"""
        -------------------
        🔄SCORES : {score}
        -------------------""")
        print(f" 🅰 : {view_entity(entity_a)}")
        entity_b = get_random_entity(entities_data_set)
        while are_entities_same(entity_a, entity_b):
            entity_b = get_random_entity(entities_data_set)
        print(vs)
        print(f" 🅱 : {view_entity(entity_b)}")
        user_answer = input("🌌Which one has more followers A or B : ").upper()
        if user_answer == "A":
            answer_is_correct = compare_entities_follower_count(greater_e=entity_a, lesser_e=entity_b)
        elif user_answer == "B":
            answer_is_correct = compare_entities_follower_count(greater_e=entity_b, lesser_e=entity_a)
        else:
            print("🤨Invalid Input, Type A or B only!")
            continue
        if answer_is_correct:
            print("🤩 You got that right!, Keep going!")
            score += 1
            entity_a = entity_b
        else:
            print("Sorry!, You got that wrong! Try again later. 💀")


# --------- MAIN ----------
game()
