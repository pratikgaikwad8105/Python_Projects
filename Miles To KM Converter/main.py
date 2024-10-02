from tkinter import *

window = Tk()
window.minsize(300, 170)
window.title("Mile To KM Converter")
window.config(padx=30, pady=20)


# Button Function
def onclick():
    kilometer = (float(distance.get()) * 1.609).__round__(2)
    label3 = Label(text=f"{kilometer}", font=20)
    label3.grid(column=1, row=1)


# Entry
distance = Entry()
distance.grid(column=1, row=0)

# Title
label1 = Label(text="Miles", font=20)
label1.grid(column=2, row=0, padx=10, pady=10)

label2 = Label(text="is equal to ", font=20)
label2.grid(column=0, row=1)


label4 = Label(text="KM", font=20)
label4.grid(column=2, row=1)

# Button
button = Button(text="Convert", command=onclick, font=20)
button.grid(column=1, row=2, padx=20)


window.mainloop()
