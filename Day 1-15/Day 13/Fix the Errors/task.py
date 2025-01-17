try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered a non-integer value, enter some number like 18.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
