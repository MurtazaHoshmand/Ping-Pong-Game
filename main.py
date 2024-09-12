import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")


is_on = True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect with boundaries
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect with the paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # right paddle miss the ball
    if ball.xcor() > 400 :
        ball.reset_position()
        score.left_point()

    # left paddle miss the ball
    if ball.xcor() < -400:
        ball.reset_position()
        score.right_point()













screen.exitonclick()