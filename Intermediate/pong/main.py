from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")
screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

game_on = True

while game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()
  
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
    
  if ball.distance(player_1) <50 and ball.xcor() > 330 or ball.distance(player_2) < 50 and ball.xcor() < -330:
    ball.block()
    
  if ball.xcor() > 380:
    scoreboard.player_2_score()
    player_1.scored()
    player_2.scored()
    ball.score()
    
  if ball.xcor() < -380:
    scoreboard.player_1_score()
    player_1.scored()
    player_2.scored()
    ball.score()
    

screen.exitonclick()