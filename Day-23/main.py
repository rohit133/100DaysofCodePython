import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tim.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    

    # Detecting weather the Player has reached the finsih line
    if tim.is_at_finish():
        tim.goto_start()
        car_manager.level_up()
        score.upgrade_level()


    # Detecting the collision with the car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            score.game_over()


    

screen.exitonclick()