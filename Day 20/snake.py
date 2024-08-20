from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def move(self):
        # move snake, perulangan berikut akan menimpa segment terakhir ke segment pertama
        for seg_num in range(len(self.segments)-1, 0,-1):
            new_x =  self.segments[seg_num-1].xcor()
            new_y =  self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # end move snake
        
        # segment 1 jalan dan yang lainnya akan mengikuti
        self.segments[0].forward(MOVE_DISTANCE)
    
    