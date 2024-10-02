from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    to_learn = original_words.to_dict(orient="records")
current_card = {}


def flip_card():
    try:
        canvas.itemconfig(word, text=current_card["English"], fill="white")
        canvas.itemconfig(title, text="English", fill="white")
    except KeyError:
        pass
    else:
        canvas.itemconfig(front_image, image=back_card)


def next_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(front_image, image=front_card)
    timer = window.after(3000, func=flip_card)


def is_known():
    try:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/Words_to_learn.csv", index=False)
    except ValueError:
        next_word()
    else:
        next_word()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

front_card = PhotoImage(file="images/card_front.png")
front_image = canvas.create_image(400, 263, image=front_card)

back_card = PhotoImage(file="images/card_back.png")

canvas.grid(row=0, column=0, columnspan=3)

# Text
title = canvas.create_text(400, 150, text="Text", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))


# Buttons

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)


window.mainloop()
