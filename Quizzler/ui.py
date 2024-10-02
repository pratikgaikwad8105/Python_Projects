from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"Score :0", font=("Arial", 15, "normal"), bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Quiz",
                                                font=("Arial", 20, "italic"),
                                                fill="black",
                                                width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0,
                                  command=self.true_press)
        self.true_button.grid(column=0, row=2)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0,
                                   command=self.false_press)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
            self.label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text=f"All Questions are Completed\nScore:{self.quiz.score-1}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
