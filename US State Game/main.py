import turtle
import pandas

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

states_list = data.state.tolist()
Guessed_states = []

while len(Guessed_states) < 50:
    answer = turtle.textinput(title=f"{len(Guessed_states)}/50 is Correct", prompt="What's the State? ").title()
    if answer == "Exit":
        missed_states = [states for states in states_list if states not in Guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("need_to_learn.csv")
        break
    if answer in states_list and answer not in Guessed_states:
        Guessed_states.append(answer)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        row = data[data.state == answer]
        state.goto(int(row.x), int(row.y))
        state.write(answer, font=("Arial", 8, "normal"))
