from turtle import Turtle, Screen

tt = Turtle()
sc = Screen()
tt.speed("fastest")


def move_forward():
    tt.forward(10)


def move_backward():
    tt.backward(10)


def turn_right():
    tt.right(5)


def turn_left():
    tt.left(5)


def clear():
    tt.clear()
    tt.penup()
    tt.home()
    tt.pendown()


sc.listen()
sc.onkey(key="d", fun=move_forward)
sc.onkey(key="a", fun=move_backward)
sc.onkey(key="w", fun=turn_left)
sc.onkey(key="s", fun=turn_right)
sc.onkey(key="c", fun=clear)

sc.mainloop()
