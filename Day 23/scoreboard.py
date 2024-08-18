FONT = ("Courier", 20, "normal")
SPEED = 0.1
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.level = 1
        self.game_speed = SPEED
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)
        
    def update_level(self):
        self.level+=1
        self.game_speed *= 0.9
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)
