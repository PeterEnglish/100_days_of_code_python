import time
from turtle import Screen, Turtle

from Snake import Snake
from Food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
segments = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on=True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()





