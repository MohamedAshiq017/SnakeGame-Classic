from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
with open("data.txt",mode = "r") as file:
  content=file.read()

class Score(Turtle):
  def __init__(self):
    super().__init__()
    print(content)
    self.score=-1
    self.high_score=content
    self.color("black")
    self.pencolor("white")
    self.hideturtle()
    self.penup()
    # self.shape("None")
    self.goto(0,270)
    self.update()


  def update(self):
    self.clear()
    self.score+=1
    self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT, font=FONT,move=False)

  def reset(self):
    if self.score > int(self.high_score):
      self.high_score=self.score
      with open ("day 24\data.txt",mode='w') as wfile:
        wfile.write(str(self.high_score))
      
    self.score=0
    self.update()

  # def gameover(self):
  #       self.goto(0,0)
  #       self.write("GAME OVER",align=ALIGNMENT, font=FONT,move=False)



