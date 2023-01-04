BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

new_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def choose_new_card():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_card["French"], fill="black")
    canvas.itemconfig(card_background, image=french_flashcard_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_card["English"], fill="white")
    canvas.itemconfig(card_background, image=eng_flashcard_image)


def right_button_pressed():
    to_learn.remove(new_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    choose_new_card()


#------------------------------------UI---------------------------------#

window = Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(800,526)
flip_timer = window.after(3000, flip_card)

language_font = ("Ariel",40,"italic")
word_font = ("Ariel", 60, "bold")


french_flashcard_image = PhotoImage(file="images/card_front.png")
eng_flashcard_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_background = canvas.create_image(400,263,image=french_flashcard_image)
card_language = canvas.create_text(400,150,font=language_font, text="Hungarian")
card_word = canvas.create_text(400,263,font=word_font, text="word")
canvas.grid(row=0,column=0, columnspan=2)



right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, width=100, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=right_button_pressed)
right_button.grid(row=1, column=0)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=choose_new_card)
wrong_button.grid(row=1, column=1)

choose_new_card()


window.mainloop()

