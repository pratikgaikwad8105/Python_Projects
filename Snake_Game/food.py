from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        food_x = randint(-280, 280)
        food_y = randint(-280, 260)
        self.goto(food_x, food_y)
