from turtle import Screen
from snake import Snake
from food import Food
import time
from scorecard import Scorecard

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Scorecard()


sc.listen()

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")
speed = 0.2
while game_on:
    sc.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 15:
        speed -= 0.005
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        speed = 0.2
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            speed = 0.2
            score.reset()
            snake.reset()

sc.mainloop()
