import random
import turtle as t
""" import colorgram 

colours = colorgram.extract("./Intermediate/turtle_painter/Nox.png", 10)

dots = []
for colour in colours:
  r = colour.rgb.r
  g = colour.rgb.g
  b = colour.rgb.b
  dots.append((r, g, b)) """

t.colormode(255)

colour_list = [(38, 29, 24), (15, 14, 36), (22, 16, 18), (121, 157, 211), (85, 97, 214), (69, 89, 157), (37, 39, 143), (103, 84, 58), (146, 168, 250), (239, 240, 233)]

timo = t.Turtle()
timo.hideturtle()
timo.pu()
row = -300

for r in range(10):
  row +=50
  timo.teleport(-250, row)
  for c in range(10):
    colour = random.choice(colour_list)
    timo.dot(20, colour)
    timo.fd(50)
    

screen = t.Screen()
screen.exitonclick()
