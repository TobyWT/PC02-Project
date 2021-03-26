import tkinter as tk


class Canvas:
    def __init__(self):
        self.root = tk.Tk()
        #self.root.geometry("400x400")
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.create_oval(200, 200, 600, 600)
        self.canvas.create_oval(300, 300, 500, 500)
        self.canvas.create_oval(450, 200, 450, 200)
        self.canvas.create_oval(150, 200, 150, 200)
        self.canvas.pack()
        self.root.mainloop()


Canvas()
