from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.turtlesize(5, 1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 245:
            ycor = self.ycor() + 45
            self.goto(self.xcor(), ycor)

    def move_down(self):
        if self.ycor() > -220:
            ycor = self.ycor() - 45
            self.goto(self.xcor(), ycor)
