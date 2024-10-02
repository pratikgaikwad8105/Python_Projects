import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car = CarManager()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_cars()
    car.move_forward()

    # Detect collision
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False
    
    # Detect crossline
    if player.ycor() > 300:
        score.increase_level()
        player.repos()
        car.increase_speed()

screen.exitonclick()
