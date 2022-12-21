from turtle import Screen, Turtle, circle
import time
import random
import turtle
from paddle import Paddle
from circle import Circle
from scorecard import Scoreboard
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")

circle = Circle()
score = Scoreboard()
screen.listen()
screen.onkey(r_paddle.move_up,"w")
screen.onkey(r_paddle.move_down,"s")
screen.onkey(l_paddle.move_up,"5")
screen.onkey(l_paddle.move_down,"2")
game_is_on = True
while game_is_on:
    time.sleep(circle.move_speed)
    screen.update()
    circle.move()

    if circle.ycor()>280 or circle.ycor()<-280:
        circle.bounce_y()
    if circle.distance(r_paddle)<50 and circle.xcor()>340 or circle.distance(l_paddle)<50 and circle.xcor()<-340:
        circle.bounce_x()
    if circle.xcor()>380 or circle.xcor()<-380:
        circle.reset_postion()
        score.l_point()
    if  circle.xcor()<-380:
        circle.reset_postion()    
        score.r_point()

screen.exitonclick()
