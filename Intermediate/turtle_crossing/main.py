import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timo = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timo.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
      if car.distance(timo) < 20:
        scoreboard.game_over()
        game_is_on = False
        
    if timo.is_safe():
      timo.goto_start()
      car_manager.level_up()
      scoreboard.increase_level()

screen.exitonclick()