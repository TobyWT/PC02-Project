from tkinter import *
from random import choice
from random import shuffle


class JumbleGame:

    def __init__(self):
        self.sec = 5
        self.e_get = ""
        self.chosen_word = ""
        self.shuffled_word = ""

        self.root = Tk()
        # Added Stuff
        self.playing = True
        self.timer = BooleanVar()
        #############
        self.root.title("Anagram Game")
        self.root.geometry("600x400")
        self.label_time = Label(self.root, text=self.sec)

        self.my_label = Label(self.root, text="", font=("Helvetica", 48), pady=20)
        self.my_label.pack()
        self.label_time.pack()

        self.my_button = Button(self.root, text="pick another word", command=self.shuffler)
        self.my_button.pack(pady=20)
        self.ans_button = Button(self.root, text="Enter", command=self.answer)
        self.ans_button.pack()
        self.e = Entry(self.root, font=("Helvetica", 20))
        self.e.pack(pady=20)
        self.answer_label = Label(self.root, text="", font=("Helvetica", 18))
        self.answer_label.pack(pady=20)
        self.shuffler()

        # ADDED THIS!
        self.timer_function()
        #####################
        self.root.mainloop()

    # ADDED THIS FUNCTION!!!!!!!!!!
    def timer_function(self):
        time=self.sec
        self.timer.set(True)
        self.label_time.config(text=time)
        while time > 0:
            self.label_time.after(1000, lambda: self.timer.set(True))
            self.label_time.wait_variable(self.timer)
            time -= 1
            self.label_time.config(text=time)
        self.timer.set(False)
        self.label_time.config(text="Time is UP!")
        self.answer_label.config(text="Time is UP!")
        self.playing = False

    def answer(self):
        if not self.playing:
            return
        self.e_get = self.e.get()
        if self.e_get == self.chosen_word:
            self.answer_label.config(text="correct")
            self.shuffler()
        else:
            self.answer_label.config(text="incorrect")

    def shuffler(self):
        if not self.playing:
            return
        list_words = ["aeroplane", "alien", "alphabet", "ambidextrous", "analogue", "analysis", "anatomy",
        "anticlockwise", "atom", "bubble", "banana", "barracks", "barricade", "behaviour", "blueberry"
        ]

        list_words = ["alien"]

        self.chosen_word = choice(list_words)

        break_apart_word = list(self.chosen_word)
        shuffle(break_apart_word)
        self.shuffled_word = ""
        for letter in break_apart_word:
            self.shuffled_word += letter
            self.my_label.config(text=self.shuffled_word)


JumbleGame()
