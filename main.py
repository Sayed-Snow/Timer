import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 6
tick_sym = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    heading.config(text='Timer')
    canvas.itemconfig(time, text='00:00')
    tick.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps, tick_sym
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text='Break', fg=RED)
        reps = 1
        tick_sym = ''
        tick.config(text=tick_sym)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text='Break', fg=PINK)
        reps += 1
        tick_sym += '✔'
        tick.config(text=tick_sym)
    else:
        count_down(work_sec)
        heading.config(text='Work', fg=GREEN)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global tick_sym, timer
    sec = count % 60
    minutes = math.floor(count/60)
    if sec < 10:
        sec = f'0{sec}'
    if minutes < 10:
        minutes = f'0{minutes}'
    canvas.itemconfig(time, text=f'{minutes}:{sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Pormodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Label
heading = tk.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
tick = tk.Label( bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10))

# Label position
heading.grid(row=1, column=2)
tick.grid(row=4, column=2)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
time = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

# Canvas position
canvas.grid(row=2, column=2)

# Buttons
start_button = tk.Button(text='Start', command=start, highlightthickness=0)
reset_button = tk.Button(text='Reset', command=reset_timer, highlightthickness=0)

# Buttons position
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)


window.mainloop()
