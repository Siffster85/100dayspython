import turtle as t

timo = t.Turtle()
screen = t.Screen()

def move_forwards():dsd
  timo.forward(5)
  
def move_backwards():
  timo.backward(5)

def turn_left():
  timo.left(5)

def turn_right():
  timo.right(5)
  
def reset():
  screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()