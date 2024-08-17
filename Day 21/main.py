from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    x_pos = snake.head.xcor()
    y_pos = snake.head.ycor()
    
    # detect collison with wall
    if x_pos > 280 or x_pos < -280 or y_pos > 280 or y_pos < -280:
        score.game_over()
        game_is_on = False
        
    #detect collison with tail
    # jumlah segment akan dipotong dari list 1 hingga terakhir, jika kepala(segment 1 pada list) menyentuh bagian segment lain dengan jarak dibawah 10 pixel maka game akan berakhir.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()