from html import escape
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizeInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        # Scoreboad 
        self.score_label = Label(text="Score:0")
        self.score_label.config(background=THEME_COLOR,font=("Arial",15),fg="white")
        self.score_label.grid(padx=20, pady=20,row=0, column=1)


        # Canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text="Some text here",fill=THEME_COLOR,font=("Arial",15,"italic"),width=280)
        self.canvas.grid(padx=20, pady=20,row=1,column=0,columnspan=2)



        # buttons 
        self.correct_img = PhotoImage(file="Day-34\\images\\true.png")
        self.wrong_img = PhotoImage(file="Day-34\\images\\false.png")
        self.correct_btn = Button(image=self.correct_img,highlightthickness=0,command=self.true_pressed)
        self.correct_btn.grid(padx=20, pady=20,row=2, column=0)
        self.wrong_btn = Button(image=self.wrong_img,highlightthickness=0,command=self.false_pressed)
        self.wrong_btn.grid(padx=20, pady=20,row=2, column=1)

        self.get_next_question()
        


        self.window.mainloop() 


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text )
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the Quiz.")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

