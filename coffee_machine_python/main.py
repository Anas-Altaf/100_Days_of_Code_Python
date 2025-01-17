from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    prompt = ""
    items_name = menu.get_items()
    while prompt != "off":
        prompt = input(f"What would you like ? ({items_name}) : ").lower()
        if prompt == "off":
            print("Shutting down, Thank you for using our services")
            return
        elif prompt == "report":
            coffee_maker.report()
            money_machine.report()
        elif menu.find_drink(prompt):
            item = menu.find_drink(prompt)
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
        else:
            print("Invalid input, Try again please")

coffee_machine()