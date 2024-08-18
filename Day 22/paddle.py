from turtle import Turtle

WIDTH = 1
HEIGHT = 5

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.create_paddle(self.x_pos, self.y_pos)
        
    def create_paddle(self, x, y):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.penup()
        self.goto(x,y)
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_pos, new_y)
