from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
  
  def __init__(self):
    self.all_cars = []
    self.speed = STARTING_MOVE_DISTANCE
    
  def create_car(self):
    random_chance = random.randint(1, 6)
    if random_chance == 1:
      car = Turtle(shape="square")
      car.shapesize(stretch_wid=0.9, stretch_len=2)
      car.pu()

      car.color(random.choice(COLORS))
      random_y = random.randint(-12, 12) * 20
      car.goto(300, random_y)
      self.all_cars.append(car)
    
  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.speed)
      
  def level_up(self):
    self.speed += MOVE_INCREMENT
    
