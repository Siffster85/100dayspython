from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 64, "normal")

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.player_1 = 0
    self.player_2 = 0
    self.color("white")
    self.ht()
    self.pu()
    self.update_score()
    
  def update_score(self):
    self.goto(-100, 200)
    self.write(f"{self.player_2}", False, align=ALIGNMENT, font=FONT)
    self.goto(100, 200)
    self.write(f"{self.player_1}", False, align=ALIGNMENT, font=FONT)
    
  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
  
  def player_1_score(self):
    self.player_1 += 1
    self.clear()
    self.update_score()
    
  def player_2_score(self):
    self.player_2 += 1
    self.clear()
    self.update_score()