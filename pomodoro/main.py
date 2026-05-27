from tkinter import *
import math
import os

os.chdir(os.path.dirname(__file__))  # set working directory to the script's folder

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 40
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 45
reps = 0
timer = None  # holds the after() reference so it can be cancelled on reset

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # add padding and set background color

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)  # cancel the scheduled countdown tick
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")  # reset the timer display
    checkmarks.config(text="")  # clear the checkmarks
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # long break every 8th rep (after 4 work sessions)
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        window.lift()  # bring window to front
        window.focus_force()  # force keyboard focus to the window
    elif reps % 2 == 0:  # short break on every other even rep
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
        window.lift()
        window.focus_force()
    else:  # odd reps are work sessions
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        window.lift()
        window.focus_force()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global marks
    global timer
    count_min = math.floor(count / 60)  # get the minutes portion of the remaining time
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # pad single-digit seconds with a leading zero

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # schedule next decrement in 1 second
    else:
        start_timer()  # automatically start the next session
        if reps % 2 == 0:  # only update checkmarks after work sessions (even reps)
            marks = ""
            work_sessions = math.floor(reps / 2)  # each pair of reps = one work session
            for i in range(work_sessions):
                marks += "✔"
            checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

title_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # load the tomato background image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # timer text displayed on the tomato image
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0, padx=0, pady=0, relief="flat", bd=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0, padx=0, pady=0, relief="flat", bd=0)
reset_button.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
