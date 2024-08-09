# from turtle import Turtle, Screen
# import another_module

# print(another_module.another_variabel)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("violet")
# timmy.goto(100, y=0)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["charmander", "Fire"],
])
table.align = "l"

print(table.get_string())