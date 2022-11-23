import random
from tkinter import *
from turtle import fillcolor

# import csv
# import pandas as pd
# nouns = pd.read_csv('100_common_nouns.csv', delimiter=',')
# print(nouns)
nouns = ["elephant", "dog", "dragon", "pony", "man","thing", "woman", "child", "python", "unicorn", "Vogon", "pencil"]
adjectives = ["Bleak", "Inimitable", "Hapless", "Happy", "Pleasant", "Infinite", "Jolly", "Honourable", "Squishy", "Lumpy"]
verbs = ["lolloping", "jumping", "crunching", "entreating", "hiding", "swishing", "sloshing", "squishing", "plashing"]

# To make a diamante poem:
# def make_line():
#     one_line = random.choice(nouns)
#     line_two = random.choice(adjectives) + " " + random.choice(adjectives)
#     line_three = random.choice(verbs) + " " + random.choice(verbs) + " " + random.choice(verbs)
#     line_four = random.choice(nouns) + " " + random.choice(nouns) + " " + random.choice(nouns) + " " + random.choice(nouns)
#     line_five = random.choice(verbs) + " " + random.choice(verbs) + " " + random.choice(verbs)
#     line_six = random.choice(adjectives) + " " + random.choice(adjectives)
#     line_seven = random.choice(nouns)
#     poem_lines = one_line + "\n" + line_two + "\n" + line_three + "\n" + line_four + "\n" + line_five + "\n" + line_six + "\n" + line_seven
#     return poem_lines

# new_poem = make_line()

window = Tk()
window.title("Prostetnic Vogon Jeltz Says - Click on my photo for more poetical delights!")
window.config(padx=20, pady=20)

canvas = Canvas(width=500, height=400)
background_img = PhotoImage(file="background.png")
canvas.create_image((500, 500), image=background_img)
quote_text = canvas.create_text(250, 250, text="Click the Vogon --->", width=500, font=("Times", 20), fill="black")
canvas.grid(row=0, column=0)

def get_quote():
    new_poem = ''
    def make_line():
        poem_lines = ""
        for n in range(3):
            poem_lines += random.choice(adjectives) + " " + random.choice(nouns) + " " + random.choice(verbs) + "\n"
        return poem_lines
    new_poem = make_line()
    canvas.itemconfig(quote_text, text=new_poem)
get_quote()
    



vogon_img = PhotoImage(file="vogon.png")

vogon_button = Button(image=vogon_img, highlightthickness=0, command=get_quote, height= 400, width =400)

vogon_button.grid(row=0, column=1)



window.mainloop()


