import math
import turtle
import colorgram
import heroes
import villains
import random
from turtle import Turtle, Screen, colormode
tim = Turtle()
tim.shape('arrow')
tim.color('blue')
colors = ['red', 'blue', 'green']
directions = [90, 180, 270, 360]
colormode(255)
tim.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_random_walk():
    tim.pensize(20)

    while True:
        tim.color(random_color())
        tim.forward(50)
        tim.hideturtle()
        tim.setheading(random.choice(directions))
        tim.showturtle()


def draw_shapes(sides):
    while sides<10:
        tim.color(random.choice(colors))
        for _ in range(sides):
            tim.forward(50)
            tim.right(360/sides)
        sides+=1


def draw_dashed_line():
    for _ in range(4):
        for _ in range(10):
            tim.forward(5)
            tim.penup()
            tim.forward(5)
            tim.pendown()
        tim.right(90)

def spirograph(gapsize):
    for _ in range(int(360/gapsize)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading()+gapsize)


def extract_colors():
    c_g_colors = colorgram.extract('jpg.jpg', 30)
    rgb_colors = []
    for color in c_g_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return(rgb_colors)

def draw_dots(colors):
    for color in colors:
        tim.color(color)
        tim.dot(10, color)
        tim.forward(len(colors)/5)

if __name__ == '__main__':
    #draw_shapes(4)
    #draw_dashed_line()
    #draw_random_walk()
    colors = extract_colors()
    draw_dots(colors)
    #spirograph(20)
    s = Screen()
    s.exitonclick()

