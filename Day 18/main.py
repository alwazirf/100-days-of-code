from turtle import Turtle, Screen
from random import choice

tim = Turtle()

tim.shape("turtle")

colours = ["light steel blue", "blue", "pale green", "burlywood", "rosy brown", "medium violet red", "medium orchid", "deep pink"]

directions = [0, 90, 180, 270]

def draw_line(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(directions))


screen = Screen()
screen.exitonclick()