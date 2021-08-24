from tkinter import *
import pandas
import random
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
new_dict = {}
to_learn = {}
try:
    data = pandas.read_csv("data/all_word_I_know.CSV UFT-8(Comma delimited)")
except FileNotFoundError:
    original_data = pandas.read_csv("data/flash_csv21.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

print(to_learn)

def choice_english_word():
    global flip_timer, new_dict
    window.after_cancel(flip_timer)
    # Old Solution
    # data = pandas.read_csv("data/flash_csv2.csv")
    # new_dict = {row.English: row.Arabic for (index, row) in data.iterrows()}
    # for key in new_dict:
    #     key_list.append(key)
    # print(key_list)
    # print(len(key_list))
    new_dict = random.choice(to_learn)
    # print(new_dict)
    canvas.itemconfig(language_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=new_dict["English"], fill="black")

    canvas.itemconfig(card_back_image, image=card_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global new_dict
    canvas.itemconfig(word_text, text=new_dict["Arabic"], fill="white")
    canvas.itemconfig(language_text, text="Arabic", fill="white")
    canvas.itemconfig(card_back_image, image=card_image_result)


def is_know():
    to_learn.remove(new_dict)
    print(len(to_learn))
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/all_word_I_know.csv", index=False)
    choice_english_word()


window = Tk()
window.title("Flash Card Game")
# window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
window.config()
# flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=1000, height=851, bg=BACKGROUND_COLOR, highlightthickness=0)

background_image = ImageTk.PhotoImage(Image.open(r"D:\Londen app\program\day-31-start\flash_card_dev\images\1study.jpg"))
canvas.create_image(0, 0, image=background_image, anchor=NW)
flip_timer = window.after(3000, func=flip_card)


card_image_result = PhotoImage(file=r"D:\Londen app\program\day-31-start\flash_card_dev\images\card_back.png")
canvas.create_image(500, 100, image=card_image_result)
canvas.grid(row=2, column=1, columnspan=2)

# 410, 270
card_image = PhotoImage(file=r"D:\Londen app\program\day-31-start\flash_card_dev\images\card_front.png")
card_back_image = canvas.create_image(500, 100, image=card_image)
canvas.grid(row=2, column=1, columnspan=2)


cross_image = PhotoImage(file=r"D:\Londen app\program\day-31-start\flash_card_dev\images\wrong.png")
button_cross = Button(image=cross_image, highlightthickness=0, command=choice_english_word)
button_cross.grid(row=2, column=1)

ture_image = PhotoImage(file=r"D:\Londen app\program\day-31-start\flash_card_dev\images\right.png")
button_true = Button(image=ture_image, highlightthickness=0, command=is_know)
button_true.grid(row=2, column=2)

word_text = canvas.create_text(500, 263, text="word", fill="black", font=("Arial", 40, "bold"))
language_text = canvas.create_text(500, 150, text="English", fill="black", font=("Arial", 40, "italic"))

choice_english_word()
window.mainloop()

