from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
  def __init__(self):
    self.segments=[]
    self.create_snake() 
    self.head=self.segments[0] 
    
    

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

 
  def add_segment(self,position):
      news_segment=Turtle("square")
      news_segment.color("white")
      news_segment.penup()
      news_segment.goto(position) 
      self.segments.append(news_segment)
      

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def reset(self):
    for segment in self.segments:
      segment.goto(1000,1000)
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
    # self.create_snake()
    # self.head=self.segments[0]
      
  
  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1):
      new_x=self.segments[seg_num-1].xcor()
      new_y=self.segments[seg_num-1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
    self.head.forward(20)
    
  def up(self):
    # new_heading=self.heading()+90
    if self.head.heading()!=DOWN:
      self.head.setheading(UP)
  def down(self):
    # new_heading=self.heading()+270
    if self.head.heading()!=UP:  
      self.head.setheading(DOWN)
  def right(self):
    # new_heading=self.heading()-90
    if self.head.heading()!=LEFT:
      self.head.setheading(RIGHT)
  def left(self):
    # new_heading=self.heading()-270
    if self.head.heading()!=RIGHT:
      self.head.setheading(LEFT)