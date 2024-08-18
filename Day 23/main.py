import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
cars = []
screen.listen()
screen.onkey(player.move, "Up")
i = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(score.game_speed)
    print(score.game_speed)
    
    if i % 6 == 0:
        car = CarManager((300, random.randint(-200, 260)))
        cars.append(car)
    
    for car in cars:
        car.car_move()
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False
    
    if player.ycor() > player.finish:
        player.reset_position()
        score.update_level()
        score.update_score()
        
    i += 1
    
screen.exitonclick()
