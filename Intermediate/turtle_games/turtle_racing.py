import random
import turtle as t

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Pick a colour of the rainbow: ").lower()
print(user_bet)

colours = ["red", "yellow", "orange", "green", "blue", "indigo", "violet"]
turtles = []

row=-200

for colour_name in colours:
  row+=50
  colour = colour_name
  colour = t.Turtle(shape="turtle")
  colour.color(colour_name)
  colour.pu()
  colour.teleport(-200, row)
  turtles.append(colour)

if user_bet:
  is_race_on = True
  
while is_race_on:
  for turtle in turtles:
    if turtle.xcor() > 200:
      winning_turtle = turtle.pencolor()
      is_race_on = False
      if winning_turtle == user_bet:
        print(f"Congratulations, you bet was correct! {winning_turtle.title()} won!")
      else:
        print(f"Commiserations, you bet was Wrong! {winning_turtle.title()} won!")
    else:
      random_distact = random.randint(1, 11)
      turtle.forward(random_distact)
  

screen.exitonclick()