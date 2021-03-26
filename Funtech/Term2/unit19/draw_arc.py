import tkinter as tk


class Canvas:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.create_arc(100, 100, 400, 400, start=0, extent=120, fill="red")
        self.canvas.create_arc(100, 100, 400, 400, start=120, extent=120, fill="blue")
        self.canvas.create_arc(100, 100, 400, 400, start=240, extent=120, fill="yellow")

        self.canvas.pack()
        self.root.mainloop()


Canvas()
