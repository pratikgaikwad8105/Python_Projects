import turtle
import pandas

screen = turtle.Screen()
screen.setup(720, 780)
screen.title("India State/UT Game")
screen.addshape("India_map.gif")
turtle.shape("India_map.gif")

data = pandas.read_csv("india_state_co-ordinates.csv")

states_list = data.state.tolist()
Guessed_states = []
missed_states = []
while len(Guessed_states) < 33:
    answer = turtle.textinput(title=f"{len(Guessed_states)}/{len(states_list)} is Correct", prompt="What's the State? ").title()
    if answer == "Exit":
        for states in states_list:
            if states not in Guessed_states:
                missed_states.append(states)
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


# def get_coordinates(x, y):
#     print(f"{x}, {y}")
#
#
# screen.onclick(get_coordinates)

screen.mainloop()
