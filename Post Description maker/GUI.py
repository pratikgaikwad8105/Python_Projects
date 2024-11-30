import customtkinter as CTK
from PIL import Image


class App(CTK.CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Generator")
        self.geometry("1200x680")
        self.resizable(False, False)
        self.configure(fg_color="black")

        self.sidebar = CTK.CTkFrame(self, width=300, fg_color="black")
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = CTK.CTkFrame(self, width=910, corner_radius=0)
        self.main_frame.pack( fill="both", side="left")

        self.sidebar_title_frame = CTK.CTkFrame(self.sidebar, fg_color="black", corner_radius=0)
        self.sidebar_title_frame.pack(padx=10, pady=20)

        # Images Import

        self.title_sidebar = CTK.CTkLabel(self.sidebar_title_frame, text="Menu",
                                          font=("open sans", 30, "bold"), width=160, text_color="white")
        self.title_sidebar.pack(padx=20, pady=5, fill="x")

        self.sidebar_logo = Image.open("icons/side.png")
        self.logo = CTK.CTkImage(self.sidebar_logo, size=(150, 150))
        # linkedin
        self.linkedin_logo = Image.open("icons/linkedin (1).png")
        self.logo_linkedin = CTK.CTkImage(self.linkedin_logo, size=(40, 40))
        # Instagram
        self.instagram_logo = Image.open("icons/instagram.png")
        self.logo_instagram = CTK.CTkImage(self.instagram_logo, size=(40, 40))
        # Reel
        self.reel_logo = Image.open("icons/reel.png")
        self.logo_reel = CTK.CTkImage(self.reel_logo, size=(40, 40))
        # Youtube
        self.youtube_logo = Image.open("icons/youtube.png")
        self.logo_youtube = CTK.CTkImage(self.youtube_logo, size=(40, 40))

        # Sidebar Buttons
        self.top_logo = CTK.CTkLabel(self.sidebar, text="Your Writer", image=self.logo, font=("verdana", 15), compound="top", text_color="white")
        self.top_logo.pack(padx=70, pady=30)

        # linkedin
        self.linkedin = CTK.CTkButton(self.sidebar, image=self.logo_linkedin, text="  Linkedin",
                                      font=("open sans", 25, "bold"), width=200, height=50, border_spacing=5,
                                      fg_color="black", compound="left", anchor="w", hover_color="#0077C5")
        self.linkedin.pack(padx=10, pady=10)

        # Instagram
        self.instagram = CTK.CTkButton(self.sidebar, image=self.logo_instagram, text=" Instagram",
                                      font=("open sans", 25, "bold"), width=200, height=50, border_spacing=5,
                                      fg_color="black", compound="left", anchor="w", hover_color="#0077C5")
        self.instagram.pack(padx=10, pady=10)

        self.reel = CTK.CTkButton(self.sidebar, image=self.logo_reel, text="   Reel",
                                    font=("open sans", 25, "bold"), width=200, height=50, border_spacing=5,
                                    fg_color="black", compound="left", anchor="w", hover_color="#0077C5")
        self.reel.pack(padx=10, pady=10)

        self.youtube = CTK.CTkButton(self.sidebar, image=self.logo_youtube, text="  Youtube",
                                    font=("open sans", 25, "bold"), width=200, height=50, border_spacing=5,
                                    fg_color="black", compound="left", anchor="w", hover_color="#0077C5")
        self.youtube.pack(padx=10, pady=10)


app = App()
app.mainloop()
