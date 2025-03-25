from turtle import Turtle


class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.pu()
    self.x_move = 10
    self.y_move = 10
    self.move_speed = 0.1

    
  def move(self):
    new_x =self.xcor() + self.x_move
    new_y =self.ycor() + self.y_move
    self.goto(new_x, new_y)
    
  def bounce(self):
    self.y_move *= -1
    
  def block(self):
    self.x_move *= -1
    self.move_speed *= 0.9
    
    
  def score(self):
    self.move_speed = 0.1
    self.goto(0,0)
    self.block()
    self.move()
