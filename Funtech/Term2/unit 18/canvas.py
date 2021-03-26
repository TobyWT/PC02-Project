import tkinter as tk


class Canvas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.create_line(0, 0, 200, 400)
        self.canvas.create_rectangle(100, 100, 200, 200, fill="#FF0000")
        self.canvas.create_line(400, 0, 200, 400)
        self.canvas.create_line(10, 10, 390, 0)
        self.canvas.create_oval(10, 10, 390, 0)
        self.canvas.pack()
        self.root.mainloop()


Canvas()
