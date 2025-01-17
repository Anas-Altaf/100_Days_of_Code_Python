# import turtle
# from turtle import Turtle, Screen
#
# timmy  = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.fd(105)
# print(timmy)
#
# a_screen = Screen()
# print(a_screen.canvheight)
# a_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmendar" ])
table.add_column("Type", ["Electric", "Water", "Fire" ])
table.align= "l"
print(table)
