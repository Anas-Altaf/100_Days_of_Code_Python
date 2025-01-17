from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ---------------- Functions
def calculate_coins(quarters : float | int, dimes : float | int, nickles : float | int , pennies : float | int):
    """
    quarters = $0.25,
    dimes = $0.10,
    nickles = $0.05,
    pennies = $0.01
    """
    quarters_in_dollars = 0.25 * quarters
    dimes_in_dollars = 0.10 * dimes
    nickles_in_dollars = 0.05 * nickles
    pennies_in_dollars = 0.01 * pennies
    return quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars
def get_resource(res_name):
    if res_name in resources:
        return float(resources[res_name])
    else:
        return 0
def resources_are_available(water: int | float, milk : int | float, coffee: int | float):
    insufficient = "Water"
    if water <= get_resource("water"):
        # print(f"{insufficient} is available")
        insufficient = "Milk"
        if milk <= get_resource("milk"):
            # print(f"{insufficient} is available")
            insufficient = "Coffee"
            if coffee <= get_resource("coffee"):
                # print(f"{insufficient} is available")
                return True
    print(f"Sorry there is not enough {insufficient}")
    return False
def get_flavor_ingredient(flavour, f_ingredient):
    if f_ingredient == "cost":
        return MENU[flavour][f_ingredient]
    else:
        return MENU[flavour]["ingredients"][f_ingredient]
def transaction_process(money_in_dollars : int | float, coffee_flavor):
    """
    Takes Money in dollars and returns change after payment
    :param coffee_flavor:
    :param money_in_dollars:
    :return: change
    """

    flavor_cost = get_flavor_ingredient(coffee_flavor, "cost")
    if money_in_dollars >= flavor_cost:
            resources["money"] += flavor_cost
            return float(money_in_dollars - flavor_cost)
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def refund_money(coffee_flavor):
    flavor_cost = get_flavor_ingredient(coffee_flavor, "cost")
    if resources["money"] > 0:
        resources["money"] -= flavor_cost
        if resources["money"] >= 0.0:
            return True
    return False
def deduct_resources( flavour):
    if flavour in MENU:
        resources["water"]-=get_flavor_ingredient(flavour, "water")
        resources["milk"]-=get_flavor_ingredient(flavour, "milk")
        resources["coffee"]-=get_flavor_ingredient(flavour, "coffee")
        return True
    else:
        return False
def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if "money" in resources:
        money = resources["money"]
    else:
        money = 0.0
    print(fr"""
-----------
 REPORT
-----------
Water : {water}ml
Milk : {milk}ml
Coffee : {coffee}g
Money : ${money}
    """)
def coffee_machine():
    print(logo)
    print("Welcome to Coffee Machine!")
    resources["money"] = 0
    # --------- Flavors
    cappuccino = "cappuccino"
    latte = "latte"
    espresso = "espresso"
    # --------- Coins

    prompt = ""
    while prompt != "off":
        prompt = input(f"What would you like ? ({espresso} | {latte} | {cappuccino}) : ").lower()
        if prompt == "off":
            print("Shutting down the machine, Thank you!")
            return
        elif prompt == cappuccino or prompt == latte or prompt == espresso:
            print("Please insert coins : ")
            quarters = float(input("How many quarters? : "))
            dimes = float(input("How many dimes? : "))
            nickles = float(input("How many nickles? : "))
            pennies = float(input("How many pennies? : "))
            money = calculate_coins(quarters= quarters, dimes= dimes, nickles= nickles, pennies= pennies)
            change = transaction_process(money, prompt )
            if change> 0:
                print(f"Here is the ${change:.2f} in change.")
            elif change is False:
                continue
            water = get_flavor_ingredient(prompt, "water")
            milk = get_flavor_ingredient(prompt, "milk")
            coffee = get_flavor_ingredient(prompt, "coffee")
            if resources_are_available(water=water, milk=milk, coffee=coffee):
                deduct_resources(prompt)
            else:
                refund_money(prompt)
                print("Money Refunded.")
                continue
            print(f"Here is your {prompt} ☕ Enjoy!")
        elif prompt == "report":
            print_report()
        else:
            print("Invalid prompt, please try again!")

# ----------------- MAIN
coffee_machine()