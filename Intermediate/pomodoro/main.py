from tkinter import *
import math

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(timer)
  title.config(text="Pomodoro")
  checkmarks.config(text="")
  canvas.itemconfig(timer_text, text="00:00")
  global reps
  reps = 0
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
    length = LONG_BREAK_MIN
    title.config(text="Rest", fg=RED)
  elif reps % 2 == 0:
    length = SHORT_BREAK_MIN
    title.config(text="Break", fg=PINK)
  else:
    length = WORK_MIN
    title.config(text="Work", fg=GREEN)
    
  count_down(length)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count -1)
  else:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
      marks += "✔ "
    checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=300, height=400, padx=50, pady=50, bg=YELLOW)

#Title
title = Label(text="Pomodoro", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 25, "bold"), )
title.grid(column=1, row=0)

#Main Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Intermediate/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

#Buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

#Checks
checkmarks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=3)


window.mainloop()