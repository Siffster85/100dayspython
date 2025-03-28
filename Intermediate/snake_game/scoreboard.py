from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.ht()
    self.pu()
    self.goto(0, 270)
    self.update_score()
    
  def update_score(self):
    self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)
    
  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
  
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score()