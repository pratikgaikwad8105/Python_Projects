import customtkinter as CTK
from PIL import Image
from linkedin_post_generate import Linkedin
from instagram_Post_generate import Instagram


class App(CTK.CTk):
    def __init__(self):
        # self.target_dropdown
        # self.tone_dropdown
        # self.purpose_dropdown
        # self.word_limit_slider
        # self.post_content
        super().__init__()
        self.title("Post Generator")
        self.geometry("1200x680")
        self.resizable(False, False)
        self.configure(fg_color="black")

        self.sidebar = CTK.CTkFrame(self, width=300, fg_color="black")
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = CTK.CTkFrame(self, width=910, corner_radius=0)
        self.main_frame.pack(fill="both", side="left")

        # Sidebar logo
        self.sidebar_title_frame = CTK.CTkFrame(self.sidebar, fg_color="black", corner_radius=0)
        self.sidebar_title_frame.pack(padx=10, pady=20)

        self.title_sidebar = CTK.CTkLabel(self.sidebar_title_frame,
                                          text="Menu",
                                          font=("open sans", 30, "bold"),
                                          width=160,
                                          text_color="white")
        self.title_sidebar.pack(padx=20, pady=5, fill="x")

        self.sidebar_logo = Image.open("icons/side.png")
        self.logo = CTK.CTkImage(self.sidebar_logo, size=(150, 150))

        self.top_logo = CTK.CTkLabel(self.sidebar,
                                     text="Your Writer",
                                     image=self.logo,
                                     font=("verdana", 15),
                                     compound="top",
                                     text_color="white")
        self.top_logo.pack(padx=70, pady=30)

        # Generate Logo
        self.generate_logo = Image.open("icons/button.png")
        self.logo_generate = CTK.CTkImage(self.generate_logo, size=(30, 30))

        # linkedin
        self.linkedin_logo = Image.open("icons/linkedin (1).png")
        self.logo_linkedin = CTK.CTkImage(self.linkedin_logo, size=(40, 40))

        self.linkedin = CTK.CTkButton(self.sidebar,
                                      image=self.logo_linkedin,
                                      text="  Linkedin",
                                      command=self.linkedin_generate,
                                      font=("open sans", 25, "bold"),
                                      width=200,
                                      height=50,
                                      border_spacing=5,
                                      fg_color="black",
                                      compound="left",
                                      anchor="w",
                                      hover_color="#0077C5")
        self.linkedin.pack(padx=10, pady=10)

        # Instagram
        self.instagram_logo = Image.open("icons/instagram.png")
        self.logo_instagram = CTK.CTkImage(self.instagram_logo, size=(40, 40))

        self.instagram = CTK.CTkButton(self.sidebar,
                                       image=self.logo_instagram,
                                       text=" Instagram",
                                       font=("open sans", 25, "bold"),
                                       width=200,
                                       height=50,
                                       border_spacing=5,
                                       fg_color="black",
                                       compound="left",
                                       anchor="w",
                                       hover_color="#0077C5",
                                       command=self.instagram_generate)
        self.instagram.pack(padx=10, pady=10)
        # Reel
        self.reel_logo = Image.open("icons/reel.png")
        self.logo_reel = CTK.CTkImage(self.reel_logo, size=(40, 40))

        self.reel = CTK.CTkButton(self.sidebar,
                                  image=self.logo_reel,
                                  text="   Reel",
                                  font=("open sans", 25, "bold"),
                                  width=200,
                                  height=50,
                                  border_spacing=5,
                                  fg_color="black",
                                  compound="left",
                                  anchor="w",
                                  hover_color="#0077C5",
                                  command=self.reel_generate)
        self.reel.pack(padx=10, pady=10)
        # Youtube
        self.youtube_logo = Image.open("icons/youtube.png")
        self.logo_youtube = CTK.CTkImage(self.youtube_logo, size=(40, 40))

        self.youtube = CTK.CTkButton(self.sidebar,
                                     image=self.logo_youtube,
                                     text="  Youtube",
                                     font=("open sans", 25, "bold"),
                                     width=200,
                                     height=50,
                                     border_spacing=5,
                                     fg_color="black",
                                     compound="left",
                                     anchor="w",
                                     hover_color="#0077C5",
                                     command=self.youtube_generate)
        self.youtube.pack(padx=10, pady=10)

    def linkedin_generate(self):
        self.hide_frames()
        self.linkedin_frame = CTK.CTkScrollableFrame(master=self.main_frame,
                                                     height=680,
                                                     width=900,
                                                     label_text="LinkedIn",
                                                     label_fg_color="#0077C5",
                                                     label_text_color="white",
                                                     label_font=("open sans", 30, "bold"),
                                                     border_width=5,
                                                     border_color="#0077C5",
                                                     scrollbar_button_hover_color="#0077C5",
                                                     corner_radius=15,
                                                     )
        self.linkedin_frame.pack(padx=10, pady=10)

        # Post Content
        post_content_label = CTK.CTkLabel(self.linkedin_frame, text="Post Content:", font=("Ariel", 18, "bold"), anchor="w")
        post_content_label.grid(row=0, column=0, pady=5, padx=5)
        self.post_content = CTK.CTkTextbox(self.linkedin_frame, height=100, width=400, font=("Ariel", 16))
        self.post_content.grid(row=1, column=0, padx=50, pady=5)

        # Purpose
        purpose_label = CTK.CTkLabel(self.linkedin_frame, text="Purpose:", font=("Ariel", 18, "bold"), anchor="w")
        purpose_label.grid(row=0, column=1, padx=130, pady=5)
        self.purpose_dropdown = CTK.CTkOptionMenu(self.linkedin_frame,
                                             values=["Select Purpose", "Advertisement", "Announcement", "Achievement", "Celebration",
                                                     "Event",  "Job Update"], font=("Ariel", 18, "bold"), width=250,
                                             height=75, anchor="center")
        self.purpose_dropdown.grid(row=1, column=1, padx=20, pady=5)

        # Tone Dropdown
        tone_label = CTK.CTkLabel(self.linkedin_frame, text="Tone of the post:", font=("Ariel", 18, "bold"), anchor="w")
        tone_label.grid(row=2, column=1, padx=15, pady=20)
        self.tone_dropdown = CTK.CTkOptionMenu(self.linkedin_frame,
                                          values=["Select Tone", "Professional", "Inspirational", "Casual",
                                                  "Informative"], font=("Ariel", 18, "bold"), width=250,
                                          height=75, anchor="center")
        self.tone_dropdown.grid(row=3, column=1, padx=20, pady=5)

        # Target Audience
        target_label = CTK.CTkLabel(self.linkedin_frame, text="Target Audience:", font=("Ariel", 18, "bold"), anchor="w")
        target_label.grid(row=2, column=0, padx=15, pady=20)
        self.target_dropdown = CTK.CTkOptionMenu(self.linkedin_frame,
                                            values=["Target Audience", "Colleagues", "Students", "Job Seekers",
                                                    "Clients", "General Network"], font=("Ariel", 18, "bold"), width=250,
                                            height=75, anchor="center")
        self.target_dropdown.grid(row=3, column=0, padx=20, pady=5)

        # Word Limit Slider
        self.word_limit_label = CTK.CTkLabel(self.linkedin_frame, text="Length : 40 words", font=("Ariel", 18, "bold"),
                                             )
        self.word_limit_label.grid(row=4, column=0, pady=20, columnspan=2)
        self.word_limit_slider = CTK.CTkSlider(self.linkedin_frame, from_=20, to=100, command=self.update_length,
                                          number_of_steps=8, width=600, button_hover_color="#0077C5", height=30,
                                          corner_radius=10)
        self.word_limit_slider.set(40)
        self.word_limit_slider.grid(row=5, column=0, padx=100, pady=15, columnspan=2)

        # Generate Button
        generate_button = CTK.CTkButton(self.linkedin_frame, text="   Generate", image=self.logo_generate, anchor="w",
                                        width=200, height=30, font=("Ariel", 20, "bold"), command=self.generate_linkedin_post)
        generate_button.grid(column=0, row=6, padx=5, pady=40, columnspan=2)

    def instagram_generate(self):
        self.hide_frames()
        self.instagram_frame = CTK.CTkScrollableFrame(master=self.main_frame,
                                                 height=680,
                                                 width=900,
                                                 label_text="Instagram",
                                                 label_fg_color="#8134AF",
                                                 label_text_color="white",
                                                 label_font=("open sans", 30, "bold"),
                                                 border_width=5,
                                                 border_color="#8134AF",
                                                 scrollbar_button_hover_color="#8134AF",
                                                 corner_radius=15
                                                 )
        self.instagram_frame.pack(padx=10, pady=10)

        # Post Content
        ig_post_title_label = CTK.CTkLabel(self.instagram_frame, text="Post Content:", font=("Ariel", 18, "bold"),
                                          anchor="w")
        ig_post_title_label.grid(row=0, column=0, pady=5, padx=5)
        self.ig_post_title = CTK.CTkTextbox(self.instagram_frame, height=100, width=400, font=("Ariel", 16))
        self.ig_post_title.grid(row=1, column=0, padx=50, pady=5)

        # Post Type
        type_label = CTK.CTkLabel(self.instagram_frame, text="Post Type:", font=("Ariel", 18, "bold"), anchor="w")
        type_label.grid(row=0, column=1, padx=130, pady=5)
        self.ig_type_dropdown = CTK.CTkOptionMenu(self.instagram_frame, fg_color="#8134AF", button_color="#AD49E1", button_hover_color="#7A1CAC",
                                               values=["Select Type", "Single Image", "Carousel",
                                                       "Reel", "Story", "Poll", "Giveaway", "Announcement",
                                                       "Behind the scenes", "IGTV", "Highlights"],
                                               font=("Ariel", 18, "bold"), width=250,
                                               height=75, anchor="center")
        self.ig_type_dropdown.grid(row=1, column=1, padx=20, pady=5)

        # Tone Dropdown
        ig_tone_label = CTK.CTkLabel(self.instagram_frame, text="Tone of the post:", font=("Ariel", 18, "bold"), anchor="w")
        ig_tone_label.grid(row=2, column=1, padx=15, pady=20)
        self.ig_tone_dropdown = CTK.CTkOptionMenu(self.instagram_frame,fg_color="#8134AF", button_color="#AD49E1", button_hover_color="#7A1CAC",
                                               values=["Select Tone", "Playful", "Inspirational", "Promotional",
                                                       "Casual", "Informative", "Story telling", "Minimalistic",
                                                       "Promotional",
                                                       "Educational", "Aesthetic", "Humorous"],
                                               font=("Ariel", 18, "bold"), width=250,
                                               height=75, anchor="center")
        self.ig_tone_dropdown.grid(row=3, column=1, padx=20, pady=5)

        # Target Audience
        ig_target_label = CTK.CTkLabel(self.instagram_frame, text="Target Audience:", font=("Ariel", 18, "bold"),
                                    anchor="w")
        ig_target_label.grid(row=2, column=0, padx=15, pady=20)
        self.ig_target_dropdown = CTK.CTkOptionMenu(self.instagram_frame, fg_color="#8134AF", button_color="#AD49E1", button_hover_color="#7A1CAC",
                                                 values=["Target Audience", "Influencers", "Small Business Owners", "Job Seekers",
                                                         "Travel Enthusiasts", "Pet Lovers", "Fitness Enthusiasts",
                                                         "Artists", "Tech Geeks", "Fashionistas", "Gamers"], font=("Ariel", 18, "bold"),
                                                 width=250,
                                                 height=75, anchor="center")
        self.ig_target_dropdown.grid(row=3, column=0, padx=20, pady=5)

        # Hashtag Focus
        ig_hashtag_label = CTK.CTkLabel(self.instagram_frame, text="Hashtag Focus:", font=("Ariel", 18, "bold"),
                                       anchor="w")
        ig_hashtag_label.grid(row=4, column=0, pady=20, columnspan=2)
        self.ig_hashtag_dropdown = CTK.CTkOptionMenu(self.instagram_frame, fg_color="#8134AF", button_color="#AD49E1",
                                                     button_hover_color="#7A1CAC",
                                                     values=["Hashtag  Focus",
                                                             "Trending Hashtags",
                                                             "Niche Hashtags",
                                                             "Branded Hashtags",
                                                             "Seasonal Hashtags"],
                                                     font=("Ariel", 18, "bold"),
                                                     width=250,
                                                     height=75, anchor="center")
        self.ig_hashtag_dropdown.grid(row=5, column=0, pady=5, columnspan=2)

        # Word Limit Slider
        self.ig_word_limit_label = CTK.CTkLabel(self.instagram_frame,
                                                text="Length : 40 words",
                                                font=("Ariel", 18, "bold"),
                                             )
        self.ig_word_limit_label.grid(row=6, column=0, pady=20, columnspan=2)
        self.ig_word_limit_slider = CTK.CTkSlider(self.instagram_frame,
                                                  from_=20, to=100, command=self.update_length,
                                                  number_of_steps=8,
                                                  width=600, button_color="#AD49E1",
                                                  button_hover_color="#7A1CAC", height=30,
                                                  corner_radius=10)
        self.ig_word_limit_slider.set(40)
        self.ig_word_limit_slider.grid(row=7, column=0, padx=100, pady=15, columnspan=2)

        # Generate Button
        ig_generate_button = CTK.CTkButton(self.instagram_frame, text="   Generate", image=self.logo_generate, anchor="w",
                                        width=200, height=30, font=("Ariel", 20, "bold"),
                                        command=self.generate_instagram_post, fg_color="#8134AF",
                                        hover_color="#7A1CAC",)
        ig_generate_button.grid(column=0, row=8, padx=5, pady=40, columnspan=2)

    def reel_generate(self):
        self.hide_frames()
        reel_frame = CTK.CTkScrollableFrame(master=self.main_frame,
                                            height=680,
                                            width=900,
                                            label_text="Reel",
                                            label_fg_color="#DD2A7B",
                                            label_text_color="white",
                                            label_font=("open sans", 30, "bold"),
                                            border_width=3,
                                            border_color="#DD2A7B",
                                            scrollbar_button_hover_color="#DD2A7B",
                                            corner_radius=15
                                            )
        reel_frame.pack(padx=10, pady=10)

    def youtube_generate(self):
        self.hide_frames()
        youtube_frame = CTK.CTkScrollableFrame(master=self.main_frame,
                                               height=680,
                                               width=900,
                                               label_text="Youtube",
                                               label_fg_color="#FF0000",
                                               label_text_color="white",
                                               label_font=("open sans", 30, "bold"),
                                               border_width=3,
                                               border_color="#FF0000",
                                               scrollbar_button_hover_color="#FF0000",
                                               corner_radius=15,
                                               )
        youtube_frame.pack(padx=10, pady=10)

    def hide_frames(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()

    def update_length(self, value):
        length = int(value)
        self.ig_word_limit_label.configure(text=f"Length : {length} words")

    def generate_linkedin_post(self):
        # TextBox
        textbox = CTK.CTkTextbox(self.linkedin_frame, height=400, width=750, font=("Ariel", 18))
        textbox.grid(row=7, column=0, pady=20, columnspan=2, sticky="s")

        post = Linkedin(self.post_content.get("0.0", "end"), self.purpose_dropdown.get(),
                        self.target_dropdown.get(), self.tone_dropdown.get(), int(self.word_limit_slider.get()))

        textbox.insert(CTK.END, post.response.content)

    def generate_instagram_post(self):
        # TextBox
        textbox = CTK.CTkTextbox(self.instagram_frame, height=400, width=750, font=("Ariel", 18))
        textbox.grid(row=7, column=0, pady=20, columnspan=2, sticky="s")

        post = Instagram(self.ig_post_title.get("0.0", "end"), self.ig_type_dropdown.get(),
                         self.ig_target_dropdown.get(), self.ig_tone_dropdown.get(),
                         self.ig_hashtag_dropdown.get(),
                         int(self.ig_word_limit_slider.get()))

        textbox.insert(CTK.END, post.response.content)


