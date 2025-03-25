from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("green")
    self.pu()
    self.setheading(90)
    self.goto_start()
    
  def move(self):
    self.forward(MOVE_DISTANCE)
    
  def goto_start(self):
    self.goto(STARTING_POSITION)
    
  def is_safe(self):
    if self.ycor() > FINISH_LINE_Y:
      return True
    else:
      return False