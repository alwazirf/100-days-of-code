from turtle import Turtle

ALIGNTMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", move=False, align=ALIGNTMENT, font=FONT)

        
    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()