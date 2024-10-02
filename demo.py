from tkinter import *

window = Tk()
window.title("Demo")
window.minsize(height=530, width=480)

label = Label(text="Python", font=("courier", 10, "bold"))
label.pack()


def clr():
    label.config(text="")


button = Button(text="Clear", command=clr, font=("Ariel", 20, "normal"))
button.config(font="courier")
button.pack()

entry = Entry(width=25)
entry.insert(END, "Here we go again!")
entry.pack(pady=5)
print(entry.get())

text = Text(width=50, height=10, borderwidth=5)
text.focus()
text.insert(END, "Enter Multiple text here")
text.pack(pady=2)
print(text.get("1.0", END))


spinbox = Spinbox(from_=1, to=10, width=20)
spinbox.pack()

scale = Scale(from_=0, to=50)
scale.pack()


def check_ticked():
    print(check.get())


check = IntVar()
checkbutton = Checkbutton(text="is Ticked", variable=check, command=check_ticked)
checkbutton.pack()


def radio_check():
    print(choosed.get())


choosed = IntVar()
radio1 = Radiobutton(text="Ronaldo", value=1, variable=choosed, command=radio_check)
radio1.pack()
radio2 = Radiobutton(text=" Messi ", value=2,  variable=choosed, command=radio_check)
radio2.pack()

list_l = ["Pratik", "Karan", "Omkar", "Virat", "Rohit"]

listbox = Listbox(height=50)
listbox.pack()

window.mainloop()
