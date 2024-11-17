from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)
  


snake=Snake()
food=Food()
score=Score()
screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

# snakes=[]
# end=0
# for new_snakes in range(3):
#   snake=Turtle(shape="square")
#   snake.color("white")
#   xpos=new_snakes*20
#   snake.goto(xpos,0)
#   print(xpos)
  
gameison=True

while gameison:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food)<15:
    food.refresh()
    snake.extend()
    score.update()
    

  if snake.head.xcor()>= 290 or snake.head.xcor( ) <= -290  or snake.head.ycor()>= 290  or snake.head.ycor()<= -290 :
    score.reset()
    snake.reset()

    
    
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10: 
      score.reset()
      snake.reset() 
    
   
 

screen.exitonclick()