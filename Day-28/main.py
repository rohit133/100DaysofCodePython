from os import times
import math
from tkinter import *
from tkinter import font 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_countdown = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_countdown)
    # Time 00:00
    canves.itemconfig(timer_text, text="00:00")
    # Titel Label to read "Timer"
    timer.config(text="Timer")
    # Reset CheckMarks 
    done_label.config(text="")
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_Sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text ="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text ="Break", fg=PINK)

    else:
        count_down(work_Sec)
        timer.config(text ="Work", fg=GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canves.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
        global timer_countdown
        timer_countdown = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔️"
        done_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50,bg=YELLOW)
canves = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
window.title("Pomodoro Timer")
timer= Label(text="Timer")
timer.config(font=(FONT_NAME,24, "bold"), bg=YELLOW, fg= GREEN)
timer.grid(column=1, row=0)
tomato_img = PhotoImage(file="Day-28\\tomato.png")
canves.create_image(100, 112, image=tomato_img)
timer_text = canves.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME,22,"bold"))
canves.grid(column=1, row=1)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.config(bg="white", font=(FONT_NAME, 10, "bold"),border=0)
start_button.grid(column=0,row=2)
# Timer Label 
done_label = Label(fg=GREEN,bg=YELLOW)
done_label.grid(column=1,row=3)
# Rest_button 
reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(bg="white",  font=(FONT_NAME, 10, "bold"),border=0)
reset_button.grid(column=2,row=2)



window.mainloop()