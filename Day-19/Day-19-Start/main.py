import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="Choose a turtle",prompt="Which turtle will win the race: enter a color:" )
print(user_bet)
turtles = []
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
y=200
for color in colors:
    y -= 50

    coloredTurtle = Turtle('turtle')
    coloredTurtle.penup()

    coloredTurtle.color(color)
    coloredTurtle.goto(-230, y)
    turtles.append(coloredTurtle)
is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            print(f"The winner is: {winning_color}")

        turtle.forward(random.randint(5, 20))

#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     newheading = tim.heading()+10
#     tim.setheading(newheading)
#
#
# def turn_right():
#     newheading = tim.heading() - 10
#     tim.setheading(newheading)
#
#
# def clear():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="h", fun=clear)



#when you pass a function as an input, you only pass the name
screen.exitonclick()

