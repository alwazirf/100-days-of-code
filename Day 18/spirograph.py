import random
import turtle as t


t.colormode(255)
timmy = t.Turtle()

timmy.speed("fastest")

def random_color():
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spinograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_graph)
        
draw_spinograph(5)



screen = t.Screen()
screen.exitonclick()