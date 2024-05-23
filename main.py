from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

# data = pd.read_csv("data/french_words.csv")
# data_dict = data.to_dict(orient="records")
# choice_word = choice(data_dict)
timer = None
choice_word = {}
data_dict = []
def next_card():
    global timer, choice_word, data_dict
    window.after_cancel(timer)
    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(language, text="French", fill="black")
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    choice_word = choice(data_dict)
    canvas.itemconfig(word, text=f"{choice_word["French"]}", fill="black")
    timer = window.after(3000, flash_card)

def check_right():
    next_card()
    data_dict.remove(choice_word)
    removed_df = pd.DataFrame.from_records(data_dict)
    removed_df.to_csv("data/words_to_learn.csv", index=False)


def check_wrong():
    next_card()



def flash_card():
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{choice_word["English"]}", fill="white")


window = Tk()
window.title("Flashy")
window.config(width=200, height=200, padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flash_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=card_front_img)

card_back_img = PhotoImage(file="images/card_back.png")

language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=check_wrong)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=check_right)
right_button.grid(row=1, column=1)
next_card()



window.mainloop()