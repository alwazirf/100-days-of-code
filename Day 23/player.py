STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
from car_manager import COLORS
import random

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(90)
        self.goto_start()
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def goto_start(self):
        self.goto(STARTING_POSITION)
        
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
