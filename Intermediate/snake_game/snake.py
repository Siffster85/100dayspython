from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.snake = []
    self.create_snake()
    self.head = self.snake[0]
    
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)
  
  def add_segment(self, position):
      body = Turtle(shape="square")
      body.color("white")
      body.pu()
      body.goto(position)
      self.snake.append(body)
      
  def reset(self):
    for part in self.snake:
      part.goto(1000,1000)
    self.snake.clear()
    self.create_snake()
    self.head = self.snake[0]
      
  def extend(self):
    self.add_segment(self.snake[-1].position())

  def move(self):
    for body in range(len(self.snake)-1, 0, -1):
      new_x = self.snake[body - 1].xcor()
      new_y = self.snake[body - 1].ycor()
      self.snake[body].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)