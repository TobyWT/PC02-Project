import tkinter


class ColourWindow:
    def __init__(self, col: str):
        self.__colour = col
        self.window = tkinter.Tk()
        self.window.title("Tkinter Beginnings")
        self.window.minsize(800, 600)
        self.window.config(bg=self.__colour)
        self.window.bind("<Button-1>", self.set_colour_event)
        self.window.bind("<Motion>", self.update_pos)
        self.window.bind("<KeyPress>", self.key_event)

        self.lbl = tkinter.Label(self.window)
        self.lbl.config(text=self.__colour, bg="black", fg="white", font=("Calibri", 18))
        self.lbl.pack()

        self.entry = tkinter.Entry(self.window)
        self.entry.config(font=("Calibri", 18))
        self.entry.pack()

        self.button = tkinter.Button(self.window)
        self.button.config(text="Change Colour", command=self.set_colour)
        self.button.pack()

        self.labels = []
        self.row1 = tkinter.Frame(self.window)
        self.row2 = tkinter.Frame(self.window)
        for i in range(4):
            if i % 2 == 0:
                r = self.row1
            else:
                r = self.row2
            self.labels.append(tkinter.Label(r, text="{}".format(i + 1)))
            if i % 2 == 0:
                self.labels[-1].config(bg="Black", fg="White")
            else:
                self.labels[-1].config(bg="White", fg="Black")
            self.labels[-1].pack(side=tkinter.RIGHT, ipadx=50, ipady=50)
        self.row1.pack()
        self.row2.pack()

    def get_colour(self) -> str:
        return self.__colour

    def key_event(self, event):
        k = event.keysym
        if k.upper() == "R":
            self.__colour = "RED"
        if k.upper() == "G":
            self.__colour = "GREEN"
        if k.upper() == "B":
            self.__colour = "BLUE"
        self.window.config(bg=self.get_colour())
        self.lbl.config(text=self.get_colour().upper())

    def set_colour(self) -> None:
        self.__colour = self.entry.get()
        self.window.config(bg=self.get_colour())
        self.lbl.config(text=self.get_colour().upper())

    def set_colour_event(self, event) -> None:
        self.__colour = self.entry.get()
        self.window.config(bg=self.get_colour())
        self.lbl.config(text=self.get_colour().upper())

    def start(self):
        self.window.mainloop()

    def update_pos(self, event):
        self.lbl.config(text="({}, {})".format(event.x, event.y))


my_window = ColourWindow("BLUE")
my_window.start()
