from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
import time


ball = Ball()

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.move()
    ball.check_change_direction()
screen.exitonclick()
