import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
SLATE = "496989"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SIXTY = 60
CHECK = "✓"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0 and not reps == 8:
        timer_label.config(foreground=PINK)
        timer_label.config(text="BREAK")
        countdown(SHORT_BREAK_MIN * SIXTY)
    elif not reps % 2 == 0:
        timer_label.config(foreground=GREEN)
        timer_label.config(text="WORK")
        countdown(WORK_MIN * SIXTY)
    else:
        timer_label.config(foreground=RED)
        timer_label.config(text="BREAK")
        countdown(LONG_BREAK_MIN * SIXTY)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# This is essentially a recursive function.
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # Dynamic Typing
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # .after() will call the specified function after a specified amount of time.
        # In order to cancel this at some point it has to be given a name / placed in a variable.
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            add_check = check_mark.cget("text") + CHECK
            check_mark.config(text=add_check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(600, 600)
window.config(padx=120, pady=60, bg=YELLOW)

canvas = Canvas(width=240, height=260, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(120, 120, image=tomato_image)
timer_text = canvas.create_text(120, 140, text="00:00", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=2, column=2)

timer_label = Label(text="TIMER", font=(FONT_NAME, 60, "bold"), bg=YELLOW, foreground=GREEN)
timer_label.grid(row=1, column=2)

check_mark = Label(font=(FONT_NAME, 36, "bold"), bg=YELLOW, foreground=GREEN)
check_mark.grid(row=4, column=2)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset)
reset_button.grid(row=3, column=3)

window.mainloop()
