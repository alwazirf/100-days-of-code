from turtle import Turtle

ALIGNTMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        self.speed("fastest")
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNTMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNTMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
