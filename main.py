import random
import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def get_words():
    try:
        pd = pandas.read_csv('data/french_words.csv')
    except FileNotFoundError:
        print("List of words unavailable.")
        return
    else:
        temp_dictionary = pd.to_dict(orient='records')
        return temp_dictionary


# window and canvas setup
window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

card_back_img = tk.PhotoImage(file="images/card_back.png", width=100, height=100)
right_img = tk.PhotoImage(file="images/right.png", width=100, height=100)
wrong_img = tk.PhotoImage(file="images/wrong.png", width=100, height=100)
right_button = tk.Button(image=right_img, highlightthickness=0)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

# get words
words_dictionary = get_words()
selection = random.randint(0, 100)
label_title = tk.Label(text=f"FRENCH", font=("Ariel", 40, "italic"))
label_word = tk.Label(text=f"{words_dictionary[selection]['French']}", font=("Ariel", 60, "bold"))
label_title.place(x=400, y=150)
label_word.place(x=400, y=263)

window.mainloop()
