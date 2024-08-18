from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
xpos = ball.xcor()
ypos = ball.ycor()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect collision wall
    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect collision with the paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    if ball.xcor() > 380:
        score.left_score()
        ball.reset_position()
    
    
    if ball.xcor() < -380:
        score.right_score()
        ball.reset_position()

screen.exitonclick()