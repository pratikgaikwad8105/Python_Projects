from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD/ SEARCH  ------------------------------- #

def save():
    website = website_entry.get().title()
    password = password_entry.get()
    username = username_entry.get()
    login_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="You Leaved Something Empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"Conformation({website})", message=f"Website :{website}\nUsername :{username}"
                                                                                 f"\nPassword :{password}\nIs it Ok?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    try:
                        data = json.load(file)
                        data.update(login_data)
                    except json.decoder.JSONDecodeError:
                        with open("data.json", "w") as file2:
                            json.dump(login_data, file2, indent=4)
                    else:
                        with open("data.json", "w") as file2:
                            json.dump(data, file2, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(login_data, file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(login_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                username_entry.delete(0, END)
            messagebox.showinfo(title="Congratulations", message="Password Saved Successfully")


def search():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showwarning(title="Warning!", message="You Leaved Something Empty!")
    else:
        try:
            with open("data.json", "r") as file:
                try:
                    _data = json.load(file)
                    username = _data[website]["Username"]
                    password = _data[website]["Password"]
                    messagebox.showinfo(title=f"{website}", message=f"Username: {username}\nPassword: {password}")
                except KeyError as website:
                    messagebox.showinfo(title="Check!", message=f"No Data found for {website}")
                except json.decoder.JSONDecodeError:
                    messagebox.showinfo(title="Check!", message=f"No Data found for {website}")
        except FileNotFoundError:
            with open("data.json", "w"):
                pass
            with open("data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    messagebox.showinfo(title="Check!", message=f"No Data found for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website :")
website_label.grid(column=0, row=1, pady=15)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, padx=5, pady=5)
website_entry.focus()

# Search Button
search = Button(text="Search", width=15, command=search)
search.grid(column=2, row=1)

# Email
username_label = Label(text="Email/Username :")
username_label.grid(column=0, row=2)

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

# Password

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, columnspan=1, padx=5, pady=5)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, padx=5, pady=5)

# Add Button

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

window.mainloop()
