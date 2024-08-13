import random
import turtle as t

t.colormode(255)
color_list = [(239, 241, 246), (233, 243, 239), (245, 235, 242), (242, 238, 227), (141, 174, 201), (22, 30, 46), (34, 106, 151), (207, 159, 112), (227, 211, 100), (141, 28, 61), (173, 49, 83), (211, 71, 99), (12, 163, 193), (193, 137, 169), (63, 168, 114), (136, 91, 74), (32, 60, 111), (115, 180, 110), (223, 79, 48), (191, 184, 43), (172, 209, 178), (7, 94, 111), (238, 205, 4), (78, 31, 64), (50, 144, 111), (221, 174, 192), (229, 171, 162), (143, 208, 230), (186, 184, 212), (108, 38, 36), (116, 121, 154), (84, 27, 26), (9, 103, 104)]


def random_color():
    return random.choice(color_list)

x_coor = -360
y_coor = -300

tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot+1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:  
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()


