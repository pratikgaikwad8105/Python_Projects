import random
from turtle import Turtle, Screen
import tkinter as Tk

sc = Screen()
sc.title("Turtle Racing")
sc.setup(width=720, height=480)
bet = sc.textinput(title="Bet Entry", prompt="Enter Bet On Turtle")
color = ["red", "yellow", "blue", "green", "purple", "orange"]
position = [0, 40, -40, 80, -80, 120]
racers = []

if bet :
    is_race_on = True

for index in range(6):
    tt = Turtle("turtle")
    tt.penup()
    tt.color(color[index])
    tt.goto(-280, position[index])
    racers.append(tt)

while is_race_on:
    for player in racers:
        if player.xcor() > 340:
            is_race_on = False
            if player.pencolor() == bet:
                Tk.messagebox.showinfo(title="RESULT", message=f"You Win ! {player.pencolor()} is a winner.")
            else:
                Tk.messagebox.showinfo(title="RESULT", message=f"You Lose ! {player.pencolor()} is a winner.")
        player.forward(random.randint(0, 10))

sc.exitonclick()
