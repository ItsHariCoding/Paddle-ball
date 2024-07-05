from turtle import Turtle,Screen
import main
from ball import Ball
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
r_paddle = main.Paddle((380,0))
l_paddle = main.Paddle((-380,0))
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"i")
screen.onkey(r_paddle.go_down,"k")
round = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    round.move()
    if round.ycor() > 280 or round.ycor() < -280:
        round.bounce_y()
    if round.xcor() > 350 and round.distance(r_paddle) < 50 or round.xcor() < -350 and round.distance(l_paddle) < 50:
        round.bounce_x()
    if round.xcor() > 380:
        round.reset()
    if round.xcor() < -380:
        round.reset()





screen.exitonclick()