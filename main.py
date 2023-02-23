import random
import tkinter as tk
import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
global words_dictionary
global current_card
global word_known


def get_words():
    try:
        pd = pandas.read_csv("words_you_need_to_learn.csv")
    except FileNotFoundError:
        pd = pandas.read_csv('data/french_words.csv')
        temp_dictionary = pd.to_dict(orient='records')
    else:
        temp_dictionary = pd.to_dict(orient='records')
    return temp_dictionary


def get_new_card():
    global current_card, reset_flip_timer
    window.after_cancel(reset_flip_timer)
    current_card = random.choice(words_dictionary)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_name, text="French", font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(word_picked, text=f"{current_card['French']}", fill="black")
    reset_flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_name, text="English", font=("Ariel", 40, "italic"), fill="red")
    canvas.itemconfig(word_picked, text=f"{current_card['English']}", fill="red")


def known_words():
    words_dictionary.remove(current_card)
    word_csv = pd.DataFrame(words_dictionary)
    with open("words_you_need_to_learn.csv", "w") as file:
        word_csv.to_csv(file)
    get_new_card()


# get words
words_dictionary = get_words()
current_card = random.choice(words_dictionary)
# window and canvas setup
window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = tk.PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = tk.PhotoImage(file="images/card_back.png", width=400, height=263)
reset_flip_timer = window.after(3000, flip_card)

title_name = canvas.create_text(400, 150, text=f"FRENCH", font=("Ariel", 40, "italic"))
word_picked = canvas.create_text(400, 263, text=f"{current_card['French']}", font=("Ariel", 60, "bold"))
right_img = tk.PhotoImage(file="images/right.png", width=100, height=100)
wrong_img = tk.PhotoImage(file="images/wrong.png", width=100, height=100)
right_button = tk.Button(image=right_img, highlightthickness=0, command=known_words)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=get_new_card)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
