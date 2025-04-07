from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("./Intermediate/snake_game/data.txt", encoding="utf-8") as data:
      saved_highscore = int(data.read())
    self.highscore = saved_highscore
    self.color("white")
    self.ht()
    self.pu()
    self.goto(0, 270)
    self.update_score()
    
  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)
    
  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open("./Intermediate/snake_game/data.txt", mode="w", encoding="utf-8") as data:
        data.write(f"{self.highscore}")
    self.score = 0
    self.update_score()
  
  def increase_score(self):
    self.score += 1
    self.update_score()