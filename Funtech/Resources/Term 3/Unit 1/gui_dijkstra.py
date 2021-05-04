import tkinter
class Node:
    def __init__(self):
        self.score = (2 ** 32) - 1
        self.parent = None


class Graph:
    def __init__(self, square_grid_size: int):
        # Construct the __nodes list with square_grid_size**2 the number of Nodes
        self.nodes = []
        for counter in range(square_grid_size * square_grid_size):
            self.nodes.append(Node())

        # Construct the adjacency matrix with the correct number of 0s
        self.adjacency_matrix = []
        for row_counter in range(len(self.nodes)):
            row = []
            for col_counter in range(len(self.nodes)):
                row.append(0)
            self.adjacency_matrix.append(row)

        # Go through each Node and add edges to the correct adjacent Nodes
        for node_index in range(len(self.nodes)):
            # Check to make sure we're not in the first row of the grid (and have a Node above us)
            if node_index / square_grid_size >= 1:
                self.adjacency_matrix[node_index][node_index - square_grid_size] = 1
            # Check to make sure we're not in the first column of the grid (and have a Node to the left)
            if node_index % square_grid_size != 0:
                self.adjacency_matrix[node_index][node_index - 1] = 1
            # Check to make sure we're not in the last row of the grid (and have a Node below us)
            if node_index / square_grid_size < square_grid_size - 1:
                self.adjacency_matrix[node_index][node_index + square_grid_size] = 1
            # Check to make sure we're not in the last column of the grid (and have a Node to the right)
            if node_index % square_grid_size != square_grid_size - 1:
                self.adjacency_matrix[node_index][node_index + 1] = 1

    def dijkstra(self, start_index: int, end_index: int) -> [Node]:
        start = self.nodes[start_index]
        start.score = 0
        end = self.nodes[end_index]
        later_list = [start]
        while len(later_list) > 0:
            current = later_list.pop(0)
            current_index = self.nodes.index(current)
            if current == end:
                temp = end
                path = [end]
                while temp.parent is not None:
                    temp = temp.parent
                    path.insert(0, temp)
                return path
            for col_index in range(len(self.adjacency_matrix[current_index])):
                if self.adjacency_matrix[current_index][col_index] == 1:
                    adjacent = self.nodes[col_index]
                    if adjacent.score > current.score + 1:
                        adjacent.score = current.score + 1
                        adjacent.parent = current
                        insertion_index = 0
                        while insertion_index < len(later_list):
                            if later_list[insertion_index].score > adjacent.score:
                                break
                            else:
                                insertion_index += 1
                        later_list.insert(insertion_index, adjacent)


class DijkstraProgram:
    def click_spot(self, event):
        # Get the 'row' the user clicked on
        row = int(event.y / self.__node_pixel_size)
        col = int(event.x / self.__node_pixel_size)

        # Check if the start index hasn't been set yet
        if self.__start_index == -1:
            # If not, set it, change that Node's rectangle colour, and change the message
            self.__start_index = (row * self.__square_grid_size) + col
            self.__canvas.itemconfig(self.__node_rectangles[self.__start_index], fill="#00FF00")
            self.__message_label.config(text="Click on the End Node")
        # After setting the start index, check if the end index hasn't been set yet
        elif self.__end_index == -1:
            # Make sure the end index isn't the same as the start index
            if (row * self.__square_grid_size) + col != self.__start_index:
                # If not, set it, change that Node's rectangle colour, and change the message
                self.__end_index = (row * self.__square_grid_size) + col
                self.__canvas.itemconfig(self.__node_rectangles[self.__end_index], fill="#FF0000")
                self.__message_label.config(text="Click anywhere else to find the path")
        # After setting the end index make sure we haven't already found the path
        elif not self.__found_path:
            # Run Dijkstra to find the path
            path = self.__graph.dijkstra(self.__start_index, self.__end_index)

            # Loop through each element in the path (except the first and last as they are the start/end nodes)
            for node_index in range(1, len(path) - 1):
                # Find its index in the node list
                node_index = self.__graph.nodes.index(path[node_index])

                # Change that rectangle's colour
                self.__canvas.itemconfig(self.__node_rectangles[node_index], fill="#FFAA22")

            # Stop the user finding the same path again
            self.__message_label.config(text="You're done!")
            self.__found_path = True

    def __init__(self, square_grid_size: int):
        # Get the Graph and Window/Canvas setup
        self.__square_grid_size = square_grid_size
        self.__node_pixel_size = 20
        self.__node_rectangles = []
        self.__start_index = -1
        self.__end_index = -1
        self.__found_path = False
        self.__graph = Graph(square_grid_size)
        self.__window = tkinter.Tk()
        self.__window.title("Dijkstra Program")
        self.__message_label = tkinter.Label(self.__window, font=("Calibri", 22), text="Click on the Start Node")
        self.__message_label.pack()
        self.__canvas = tkinter.Canvas(self.__window, width=square_grid_size * self.__node_pixel_size,
                                       height=square_grid_size * self.__node_pixel_size, bg="#FFFFFF",
                                       borderwidth=1, highlightbackground="#000000")
        self.__canvas.bind("<Button-1>", self.click_spot)
        self.__canvas.pack()

        # Draw the Graph onto the Canvas
        for node_index in range(len(self.__graph.nodes)):
            # Get the coordinate of the current Node
            x = (node_index % self.__square_grid_size) * self.__node_pixel_size
            y = int(node_index / self.__square_grid_size) * self.__node_pixel_size

            # Draw the current Node and save it in a list (in the same order as the Nodes) to change colour later
            rectangle = (self.__canvas.create_rectangle(x, y, x + self.__node_pixel_size, y + self.__node_pixel_size))
            self.__node_rectangles.append(rectangle)

        # Start the program
        self.__window.mainloop()


# Instantiate and start the program (using this argument for the size of the grid of Nodes)
DijkstraProgram(50)
