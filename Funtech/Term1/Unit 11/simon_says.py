import tkinter
import random


class SimonSays:
    def __init__(self):
        self.score = 0
        self.playing = True
        self.current_button = -1
        self.simon_said = True

        self.window = tkinter.Tk()
        self.window.title("Simon Says")

        self.status_label = tkinter.Label()
        self.status_label.bind("<Button-1>", self.reset)
        self.status_label.pack()

        self.rows = []
        for i in range(3):
            self.rows.append(tkinter.Frame(self.window))
            self.rows[-1].pack()
        for i in range(9):
            if i < 3:
                row = 0
            elif i < 6:
                row = 1
            else:
                row = 2
            b = tkinter.Button(self.rows[row], text=str(i+1))
            b.bind("<Button-1>", self.button_click)
            b.pack(side=tkinter.LEFT, ipadx=50, ipady=50)

    def button_click(self, event):
        if not self.playing:
            return
        num = int(event.widget.cget("text"))
        win_1 = self.simon_said and (self.current_button == num)
        win_2 = (not self.simon_said) and (self.current_button != num)
        if win_1 or win_2:
            self.score += 1
            self.generate()
        else:
            self.playing = False
            status_text = "Game Over. Final Score: {}. Click here to play again!".format(self.score)
            self.status_label.config(text=status_text)
            print(num)
            print(self.current_button)

    def generate(self):
        self.current_button = random.randint(1, 9)
        self.simon_said = random.choice([True, False])
        status_text = "Press {}".format(self.current_button)
        if self.simon_said:
            status_text = "Simon Says " + status_text
        self.status_label.config(text=status_text)

    def reset(self, event):
        if self.playing:
            return
        self.score = 0
        self.playing = True
        self.generate()

    def start(self):
        self.generate()
        self.window.mainloop()


game = SimonSays()
game.start()
