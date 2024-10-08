import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    car_manager.create_car()
    car_manager.move_cars()

    # detect colission with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            
    # detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score.increase_level()



screen.exitonclick()
