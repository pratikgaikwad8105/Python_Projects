from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
import customtkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [
                        choice(letters) for _ in range(randint(8, 10))
                    ] + [
                        choice(symbols) for _ in range(randint(2, 4))
                    ] + [
                        choice(numbers) for _ in range(randint(2, 4))
                    ]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get().title()
    password = password_entry.get()
    username = username_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="You Left Something Empty!")
        return

    is_ok = messagebox.askokcancel(title=f"Confirmation ({website})",
                                   message=f"Website: {website}\nUsername: {username}\nPassword: {password}\nIs it OK?")
    if is_ok:
        login_data = {website: {"Username": username, "Password": password}}

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}

        data.update(login_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.delete(0, END)
        messagebox.showinfo(title="Congratulations", message="Password Saved Successfully")


def search():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showwarning(title="Warning!", message="You Left Something Empty!")
        return

    try:
        with open("data.json", "r") as file:
            _data = json.load(file)
            username = _data[website]["Username"]
            password = _data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        messagebox.showinfo(title="Check!", message=f"No Data found for {website}")


def sign_in():
    global username, password
    global window, website_entry, password_entry, username_entry
    global logo
    try:
        with open("login.json", "r") as file:
            data = json.load(file)

            try:

                if username.get() == data[username.get()]["Username"] and password.get() == data[username.get()]["Password"]:
                    signin.destroy()

                    # ----------------------- Main Screen ----------------------#
                    window = Tk()
                    window.title("Password Manager")
                    window.config(padx=50, pady=50)

                    # Create a canvas for the logo
                    canvas = Canvas(window, width=200, height=200)
                    try:
                        logo = PhotoImage(file="logo.png")  # Store the logo image
                        canvas.create_image(100, 100, image=logo)  # Adjusted position for center
                        canvas.grid(column=1, row=0)
                    except Exception as e:
                        print(f"Error loading logo: {e}")

                    # Website label and entry
                    Label(window, text="Website:").grid(column=0, row=1, pady=15)
                    website_entry = Entry(window, width=30)
                    website_entry.grid(column=1, row=1, padx=5, pady=5)
                    website_entry.focus()

                    # Search button
                    Button(window, text="Search", width=15, command=search).grid(column=2, row=1)

                    # Username label and entry
                    Label(window, text="Email/Username:").grid(column=0, row=2)
                    username_entry = Entry(window, width=50)
                    username_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

                    # Password label and entry
                    Label(window, text="Password:").grid(column=0, row=3)
                    password_entry = Entry(window, width=30)
                    password_entry.grid(column=1, row=3, columnspan=1, padx=5, pady=5)

                    # Generate password button
                    Button(window, text="Generate Password", command=generate_password).grid(column=2, row=3, padx=5,
                                                                                             pady=5)

                    # Add button
                    Button(window, text="Add", width=45, command=save).grid(column=1, row=4, columnspan=2, padx=5,
                                                                            pady=5)

                    window.mainloop()  # Start the main application loop
                else:
                    messagebox.showerror(title="Login Failed", message="Invalid username or password.")
            except KeyError:
                messagebox.showerror(title="Login Failed", message="Invalid username or password.")
    except FileNotFoundError:
        with open("login.json", "w"):
            messagebox.showerror(title="Login Failed", message="Invalid username or password.")


def sign_up():
    if len(su_username.get()) == 0 or len(su_password.get()) == 0 or len(re_password.get()) == 0:
        messagebox.showerror(title="Warning!", message="You Left Something Empty!")
        return

    if su_password.get() != re_password.get():
        messagebox.showerror(title="Try Again!", message="Password Not Match!")
        return

    login_data = {su_username.get(): {"Username": su_username.get(), "Password": su_password.get()}}

    try:
        with open("login.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    data.update(login_data)

    with open("login.json", "w") as file:
        json.dump(data, file, indent=4)

    signup.destroy()
    sign_in_window()


def sign_up_button():

    global su_username, su_password, re_password, signup

    signin.destroy()
    signup = customtkinter.CTk()
    signup.title("Signup")
    signup.geometry("400x400")
    signup.resizable(False, False)

    su_frame = customtkinter.CTkFrame(master=signup)
    su_frame.grid(padx=30, pady=30)

    su_label = customtkinter.CTkLabel(master=su_frame, text="Sign up", font=("Archivo Black", 40, "bold"))
    su_label.grid(padx=20, pady=20, column=0, row=0)

    su_username = customtkinter.CTkEntry(master=su_frame, width=300, height=40, placeholder_text="Username", corner_radius=10)
    su_username.grid(padx=20, pady=10)

    su_password = customtkinter.CTkEntry(master=su_frame, width=300, height=40, placeholder_text="Password", corner_radius=10)
    su_password.grid(padx=20, pady=10)

    re_password = customtkinter.CTkEntry(master=su_frame, width=300, height=40, placeholder_text="Confirm Password", corner_radius=10)
    re_password.grid(padx=20, pady=10)

    signupbutton = customtkinter.CTkButton(master=su_frame, text="Sign Up", corner_radius=30, height=40, width=120, command=sign_up)
    signupbutton.grid(padx=20, pady=20)

    signup.mainloop()


# -------------------------------------- SignIn window ---------------------------------#
def sign_in_window():
    global signin, username, password
    signin = customtkinter.CTk()
    signin.title("Login")
    signin.geometry("420x370")
    signin.resizable(False, False)

    frame = customtkinter.CTkFrame(master=signin)
    frame.grid(padx=30, pady=30)

    label = customtkinter.CTkLabel(master=frame, text="Login", font=("Archivo Black", 40, "bold"))
    label.grid(padx=20, pady=20, column=0, row=0)

    username = customtkinter.CTkEntry(master=frame, width=300, height=40, placeholder_text="Username", corner_radius=10)
    username.grid(padx=20, pady=10)

    password = customtkinter.CTkEntry(master=frame, width=300, height=40, placeholder_text="Password", corner_radius=10)
    password.grid(padx=20, pady=10)

    inner_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
    inner_frame.grid(padx=20, pady=10)

    signin_button = customtkinter.CTkButton(master=inner_frame, text="Login", corner_radius=30, height=40, width=120, command=sign_in)
    signin_button.grid(column=0, row=0, padx=20, pady=20)

    signup_button = customtkinter.CTkButton(master=inner_frame, text="Sign Up", corner_radius=30, height=40, width=120, command=sign_up_button)
    signup_button.grid(column=1, row=0, padx=20, pady=20)

    signin.mainloop()


sign_in_window()
