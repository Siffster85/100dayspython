import random
import turtle as t

timo = t.Turtle()
t.colormode(255)
timo.shape("turtle")
timo.pensize(1)
timo.speed(0)
headings = [0, 90, 180, 270]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

""" for _ in range(4):
  timo.forward(100)
  timo.left(90)
 """

""" def draw_shape(sides):
  angle = 360 / sides
  for _ in range(sides):
    timo.forward(100)
    timo.left(angle)

for i in range(3, 11):
  timo.color(random_color())
  draw_shape(i) """

""" def random_walk(direction):
  timo.setheading(direction)
  timo.forward(25)
  
for _ in range(200):
  timo.color(random_color())
  random_walk(random.choice(headings)) """
  
def draw_spiral(heading):
  timo.setheading(heading)
  timo.circle(100)

for i in range(0, 360, 8):
  timo.color(random_color())
  draw_spiral(i)
  

screen = t.Screen()
screen.exitonclick()