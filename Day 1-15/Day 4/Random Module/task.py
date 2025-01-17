import random

# # Random Integers
# random_integer = random.randint(1,10)
# print(random_integer)
# # Random Floats - Semi Open Range - might 0
# random_float_0_to_1 = random.random()
# print(random_float_0_to_1)
#
# # Uniform Float - open range
# random_float = random.uniform(1, 10)
# print(random_float)

# Head , Tail
result  = random.randint(0,1)
if result == 1:
    print("Head")
else:
    print("Tail")