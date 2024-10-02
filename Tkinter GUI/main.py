from tkinter import *

window = Tk()
window.title("My 2nd GUI")
window.minsize(width=900, height=720)


def onclick():
    my_button.config(text="Clicked")
    my_label.config(text=_input.get())


# Label

my_label = Label(text="This Is Label", font=("Times New Roman", 25, "bold"))
my_label.grid(column=0, row=0)

# Button

my_button = Button(text="Click", command=onclick)
my_button.grid(column=1, row=1)

my_button2 = Button(text="Click", command=onclick)
my_button2.grid(column=2, row=0)
# Entry

_input = Entry()
_input.grid(row=3, column=3)


window.mainloop()
