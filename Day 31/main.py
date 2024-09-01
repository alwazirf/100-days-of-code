from tkinter import *
import pandas as pd
from random import randint, choice
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel",40, "italic")
FONT_QS = ("Ariel", 60, "bold")
to_learn = {}
current_card = {}
flip_timer = None

# ---------------------------- USING PD TO READ DATA ------------------------------- #
try:
    data_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pd.read_csv("./data/french_words.csv")
    to_learn = original_file.to_dict("records")
else:
    to_learn = data_file.to_dict("records")

# ---------------------------- Generate Random ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(question_title, text="French", fill="black")
    canvas.itemconfig(question_text, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(image_bg, image=image_front)
    flip_timer = window.after(2000, func=flip_card)

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv")
    next_card()
    
def flip_card():
    canvas.itemconfig(question_title, text="English", fill="white")
    canvas.itemconfig(question_text, text=f"{current_card["English"]}", fill="white")
    canvas.itemconfig(image_bg, image=image_back)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(2000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="./images/card_front.png")
image_bg = canvas.create_image(400,263, image=image_front)
image_back = PhotoImage(file="./images/card_back.png")
question_title = canvas.create_text(400, 150, text="", fill="black", font=FONT_TITLE)
question_text = canvas.create_text(400, 263, text="", fill="black", font=FONT_QS)
canvas.grid(row=0, column=0, columnspan=2)
# button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
next_card()

window.mainloop()