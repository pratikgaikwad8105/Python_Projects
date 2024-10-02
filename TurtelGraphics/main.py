import random
import colorgram
from turtle import Turtle, Screen, colormode

tt = Turtle()
colors = colorgram.extract('image.jpg', 30)

# # Square
# for _ in range(4):
#     tt.forward(100)
#     tt.right(90)

# # Dashed line
# for _ in range(100):
#     tt.forward(10)
#     tt.up()
#     tt.forward(10)
#     tt.down()

colormode(255)
# for i in range(3, 11):
#     for j in range(i):
#         tt.color(R, G, B)
#         tt.right(360 / i)
#         tt.forward(100)
# tt.speed("fastest")


# def change_color():
#     r = random.randrange(0, 257, 10)
#     g = random.randrange(0, 257, 10)
#     b = random.randrange(0, 257, 10)
#
#     return r, g, b


# # Random Pattern
# for _ in range(500):
#     angle = random.randrange(0, 360, 90)
#     R, G, B = change_color()
#     tt.color(R, G, B)
#     tt.setheading(angle)
#     tt.forward(35)

# for _ in range(0, 100):
#     R, G, B = change_color()
#     tt.color(R, G, B)
#     tt.left(3.6)
#     tt.circle(100)

colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    colortuple = (r, g, b)
    colors_list.append(colortuple)

tt.hideturtle()


for i in range(0, 10):
    tt.teleport(-200, -200 + (50 * i))
    for j in range(10):
        tt.dot(20, random.choice(colors_list))
        tt.up()
        tt.fd(50)

scr = Screen()
scr.exitonclick()