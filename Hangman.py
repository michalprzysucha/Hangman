from tkinter import *
from tkinter import messagebox
import random
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500


def draw_word():
    word = None

    try:
        with open("words.txt", "r") as words_file:
            lines = words_file.read().splitlines()
        word = random.choice(lines)
    except IOError:
        sys.exit("words.txt file not found!")
    return word


def guess(letter_str_var):
    letter = letter_str_var.get()
    
    if len(letter) > 1:
        messagebox.showerror("Hangman", "You can pass only single letter!")
        return
    
    

def game():
    word = draw_word()
    word_with_spaces = " ".join(word)
    unders = "".join(["_" if c != " " else c for c in word_with_spaces])

    word_state.set(unders)
    print("Wylosowano:", word)



root = Tk()
root.title('Hangman')
root.iconbitmap('./window_icon.ico')
root.resizable(False, False)

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - WINDOW_WIDTH / 2)
center_y = int(screen_height/2 - WINDOW_HEIGHT / 2)

root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')

image_label = Label(root, image=photos[11])
image_label.pack(expand=True)

word_state = StringVar()
word_state_label = Label(root, textvariable=word_state,font=("lucida", 20, "bold"))
word_state_label.pack(ipadx=5, ipady=5, expand=True)

letter = StringVar()
letter_entry = Entry(root, textvariable=letter, font=("lucida", 20, "bold"))
letter_entry.pack(ipady=5, expand=True)
letter_entry.focus()

submit_button = Button(root, text="Submit", command=lambda:guess(letter))
submit_button.pack(ipadx=5, ipady=5, expand=True)

game()
root.mainloop()