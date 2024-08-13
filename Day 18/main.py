from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()

tim.shape("turtle")

colours = ["light steel blue", "blue", "pale green", "burlywood", "rosy brown", "medium violet red", "medium orchid", "deep pink"]

colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]

def draw_line(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))




screen = Screen()
screen.exitonclick()