from turtle import Turtle

ALIGNTMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt", "r+") as data:
            self.data = data.read()
        self.score = 0
        self.high_score = int(self.data)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        self.speed("fastest")
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNTMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
