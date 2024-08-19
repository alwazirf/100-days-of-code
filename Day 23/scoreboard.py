from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.level = 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)
        
    def increase_level(self):
        self.level+=1
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)
