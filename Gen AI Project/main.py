from groq import Groq
import customtkinter
from PIL import Image

client = Groq(
    api_key="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",
)


def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        model="gemma2-9b-it",
    )

    return chat_completion


# ____________________________________UI________________________________________

def submit():

    try:
        prompt1 = f"create point wise 200 words report, each line contain format:'Nutrient Contain : Measurement(Unit)' , for food: {food_entry2.get()} , quantity : {food_entry.get()}, don't create any other extra characters in report like ** and ## and ~ and note at last."
        prompt2 = f"create less than 200 words professional suggestion report like you are diet consultant, I am {food_entry3.get("0.0", "end")} ,eat food {food_entry2.get()}  {food_entry.get()},consider a daily requirements,each line contain point each point is about is this good or bad and less than 10 words,don't create any other extra characters in report like ** and ## and ~ ."

        stat_window = customtkinter.CTk()
        stat_window.geometry("1024x600")
        stat_window.title("Statistics")
        stat_window.resizable(width=False, height=False)

        stat_view = customtkinter.CTkTabview(master=stat_window, width=200, border_width=2, border_color="grey")
        stat_view.pack(padx=20, pady=20)

        stat_view.add("Gained Nutrients")
        stat_view.add("Suggestions")

        label = customtkinter.CTkLabel(master=stat_view.tab("Gained Nutrients"), text=chat(prompt1).choices[0].message.content, font=("Poppins", 15, "normal"))
        label.grid(row=0, column=0, padx=20, pady=10)

        label = customtkinter.CTkLabel(master=stat_view.tab("Suggestions"), text=chat(prompt2).choices[0].message.content, font=("Poppins", 15, "normal"))
        label.grid(row=0, column=0, padx=20, pady=10)

        stat_window.mainloop()
    except :
        error = customtkinter.CTkToplevel(window)
        error.title("Network Error")
        error.attributes('-topmost', True)
        msg = customtkinter.CTkLabel(master=error, text="Check Internet Connection", font=("verdana", 15, "normal"))
        msg.pack(padx=20, pady=20)


window = customtkinter.CTk()
window.title("Diet Consultant")
window.geometry("1024x600")
window.resizable(width=False, height=False)
window.configure(fg_color="#FBBA00")

# Banner
banner_frame = customtkinter.CTkFrame(window, width=1024, height=150, border_color="black", border_width=0)
banner_frame.grid(column=0, row=0, sticky="nsew")

banner = customtkinter.CTkImage(light_image=Image.open("banner.jpg"), size=(1024, 150))
banner_image = customtkinter.CTkLabel(master=banner_frame, image=banner, text="")
banner_image.grid(column=0, row=0)

# body

body_Frame = customtkinter.CTkFrame(window, height=450, border_color="black", border_width=3, corner_radius=20)
body_Frame.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")

# Food Entry
food_entry_Frame = customtkinter.CTkFrame(body_Frame, border_color="black", border_width=1, corner_radius=20)
food_entry_Frame.grid(column=0, row=0, padx=20, pady=20, sticky="nw")

recipie_label = customtkinter.CTkLabel(master=food_entry_Frame, text="Recipie/Food", font=("Kanit", 20, "bold"))
recipie_label.grid(column=0, row=0, padx=5, pady=5)

food_entry = customtkinter.CTkEntry(master=food_entry_Frame, placeholder_text="Enter Food/Recipie", width=400, height=40)
food_entry.grid(column=0, row=1, padx=30, pady=20)


# Quantity
food_entry_Frame = customtkinter.CTkFrame(body_Frame, border_color="black", border_width=1, corner_radius=20)
food_entry_Frame.grid(column=1, row=0, padx=10, pady=20, sticky="nw")

quantity_label = customtkinter.CTkLabel(master=food_entry_Frame, text="Quantity", font=("Kanit", 20, "bold"))
quantity_label.grid(column=0, row=0, padx=5, pady=5)

food_entry2 = customtkinter.CTkEntry(food_entry_Frame, placeholder_text="Enter Quantity", width=400, height=40)
food_entry2.grid(column=0, row=1, padx=30, pady=20)


# Describe Food
food_description_Frame = customtkinter.CTkFrame(body_Frame, border_color="black", border_width=1, corner_radius=20)
food_description_Frame.grid(column=0, row=1, padx=20, pady=5, sticky="nw", columnspan=2)

description_label = customtkinter.CTkLabel(master=food_description_Frame, text="Description(eg.age,gender,health issue,etc)", font=("Kanit", 20, "bold"))
description_label.grid(column=0, row=0, padx=5, pady=10)

food_entry3 = customtkinter.CTkTextbox(master=food_description_Frame, width=940, height=100, corner_radius=20, border_width=2, border_color="black")
food_entry3.grid(column=0, row=1, padx=10, pady=20)

quantity = food_entry2.get()
entry = food_entry.get()
description = food_entry3.get("0.0", "end")

# Button

button = customtkinter.CTkButton(master=body_Frame, corner_radius=30, border_color="black",border_width=1, text="Submit", font=("Kanit",15,"bold" ), text_color="white", width=200, height=40,fg_color="#047652", hover_color="#FBBA00", command=submit)
button.grid(column=0, row=2, columnspan=2, pady=15)


window.mainloop()