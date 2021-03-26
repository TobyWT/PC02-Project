import tkinter


class Shape2D:
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle2D(Shape2D):
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def area(self) -> float:
        return self.__length * self.__width

    def perimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return "Rectangle[{}, {}]".format(self.__length, self.__width)


class Circle2D(Shape2D):
    PI = 3.14

    def __init__(self, rad: float):
        self.__radius = rad

    def area(self) -> float:
        return Circle2D.PI * (self.__radius ** 2)

    def perimeter(self) -> float:
        return 2 * Circle2D.PI * self.__radius

    def __str__(self):
        return "Circle[{}]".format(self.__radius)


class Triangle2D(Shape2D):
    def __init__(self, base: float, height: float):
        self.__base = base
        self.__height = height

    def area(self) -> float:
        return self.__base * self.__height * 0.5

    def perimeter(self) -> float:
        return 2 * (self.__base + self.__height)

    def __str__(self):
        return "Triangle[{}, {}]".format(self.__base, self.__height)


class ShapeWindow:
    def __init__(self):
        self.shapes = []
        self.rows = []

        self.window = tkinter.Tk()
        for i in range(3):
            self.rows.append(tkinter.Frame(self.window))
            self.rows[-1].pack()

        self.rect_label = tkinter.Label(self.rows[0], text="Rectangle: ")
        self.rect_label.pack(side=tkinter.LEFT)
        self.rect_len = tkinter.Entry(self.rows[0])
        self.rect_len.pack(side=tkinter.LEFT)
        self.rect_wid = tkinter.Entry(self.rows[0])
        self.rect_wid.pack(side=tkinter.LEFT)
        self.rect_button = tkinter.Button(self.rows[0], text="Generate", command=self.gen_rect)
        self.rect_button.pack(side=tkinter.LEFT)

        self.tri_label = tkinter.Label(self.rows[1], text="Triangle: ")
        self.tri_label.pack(side=tkinter.LEFT)
        self.tri_bas = tkinter.Entry(self.rows[1])
        self.tri_bas.pack(side=tkinter.LEFT)
        self.tri_hei = tkinter.Entry(self.rows[1])
        self.tri_hei.pack(side=tkinter.LEFT)
        self.tri_button = tkinter.Button(self.rows[1], text="Generate", command=self.gen_tri)
        self.tri_button.pack(side=tkinter.LEFT)

        self.cir_label = tkinter.Label(self.rows[2], text="Circle: ")
        self.cir_label.pack(side=tkinter.LEFT)
        self.cir_bas = tkinter.Entry(self.rows[2])
        self.cir_bas.pack(side=tkinter.LEFT)
        self.cir_button = tkinter.Button(self.rows[2], text="Generate", command=self.gen_cir)
        self.cir_button.pack(side=tkinter.LEFT)

        self.output_button = tkinter.Button(self.window, text="Output", command=self.output)
        self.output_button.pack()

    def start(self):
        self.window.mainloop()

    def gen_rect(self):
        self.shapes.append(Rectangle2D(float(self.rect_len.get()), float(self.rect_wid.get())))

    def gen_tri(self):
        self.shapes.append(Triangle2D(float(self.tri_bas.get()), float(self.tri_hei.get())))

    def gen_cir(self):
        self.shapes.append(Circle2D(float(self.tri_bas.get())))

    def output(self):
        print("Shapes:")
        for shape in self.shapes:
            print("\t{}".format(shape))


shape_window = ShapeWindow()
shape_window.start()
