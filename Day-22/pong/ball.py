from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_increment = 10
        self.y_increment = 10

    def move(self):
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)

    def collide(self):
        if self.ycor() == -300 or self.ycor() == 300:
            return True
        else:
            return False

    def check_change_direction(self):
        if self.collide():
            self.y_increment = -self.y_increment