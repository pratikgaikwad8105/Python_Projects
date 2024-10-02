from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5
        self.all_cars = []
    
    def generate_cars(self):
        chance = random.randint(1, 10)
        if chance <= 3:
            car = Turtle()
            car.setheading(180)
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(320, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)
    
    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
