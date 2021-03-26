import tkinter as tk


class Canvas:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.title_text = self.canvas.create_text(400, 100, text="Title:", font=("Calibre", 40))
        self.canvas.pack()
        self.root.mainloop()


Canvas()