import turtle

from paddle import Paddle
from ball import Ball
import time
from scorecard import Scorecard

tt = turtle.Turtle()
sc = turtle.Screen()
image = "image.gif"
sc.addshape(image)
tt.shape(image)

sc.listen()
sc.setup(1000, 800)
sc.title("Pong")
sc.bgcolor("black")
sc.tracer(0)

paddle1 = Paddle(370, 0, "red")
paddle2 = Paddle(-370, 0, "blue")
ball = Ball()
score = Scorecard()


sc.onkeypress(paddle1.move_up, "Up ")
sc.onkeypress(paddle1.move_down, "Down")

sc.onkeypress(paddle2.move_up, "w")
sc.onkeypress(paddle2.move_down, "s")

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    sc.update()
    ball.move()

    if ball.ycor() >= 300 or ball.ycor() <= -280:
        ball.bounce_y()
    
    if ball.distance(paddle1) <= 50 and ball.xcor() >= 350 or ball.distance(paddle2) <= 50 and ball.xcor() <= -350:
        ball.bounce_x()

    if ball.xcor() > 400:
        score.r_point()
        ball.reset_position()
    
    if ball.xcor() < -400:
        score.l_point()
        ball.reset_position()

sc.exitonclick()
