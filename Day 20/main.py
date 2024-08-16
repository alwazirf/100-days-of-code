from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

obanai = Snake()
screen.listen()
screen.onkey(obanai.up, "Up")
screen.onkey(obanai.down, "Down")
screen.onkey(obanai.left, "Left")
screen.onkey(obanai.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    obanai.move()


screen.exitonclick()