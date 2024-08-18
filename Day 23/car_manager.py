COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.x_pos = pos[0]
        self.y_pos = pos[1] 
        self.create_car()
        
    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(self.x_pos, self.y_pos)
    
    def car_move(self):
        new_xpos = self.xcor() - MOVE_INCREMENT
        self.goto(new_xpos, self.y_pos)

