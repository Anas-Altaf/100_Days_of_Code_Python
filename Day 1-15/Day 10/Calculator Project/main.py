from art import logo
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
use_prev_result = False
result = 0.0
while True:
    if  use_prev_result:
        n1 = result
    else:
        print(logo)
        n1 = float(input("Enter your first number : "))
    for op in operations_dict:
        print(op)
    operation = input("Enter the operation you want to perform: ")
    n2 = float(input("Enter your next number : "))
    result = operations_dict[operation](n1, n2)
    print(f"The Result : \n{n1} {operation} {n2} = {result}")
    prev_result_choice = input(
        "Type 'y' if you wanna use previous result as first number , or type 'n' if you wanna start a new operation : ").lower()
    if 'y' in prev_result_choice :
        use_prev_result = True
    else:
        use_prev_result = False
