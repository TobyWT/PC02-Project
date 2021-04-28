import random
import tkinter


class Node:
    def __init__(self):
        self.visited = False


class Graph:
    def __init__(self, maze_size: int):
        self.maze_size = maze_size
        self.nodes = []
        for count in range(maze_size * maze_size):
            self.nodes.append(Node())
        self.adjacency_matrix = []
        for row_count in range(maze_size * maze_size):
            row = []
            for col_count in range(maze_size * maze_size):
                row.append(0)
            self.adjacency_matrix.append(row)
        self.node_grid = []
        for row_count in range(maze_size):
            row = []
            for col_count in range(maze_size):
                row.append((row_count * maze_size) + col_count)
            self.node_grid.append(row)
        self.recursive_backtrack(self.nodes[0])

    def __str__(self) -> str:
        output = ""
        for row in self.node_grid:
            for col in row:
                output += str(col) + "\t"
            output += "\n"

        output += "\n\n"
        for row in self.adjacency_matrix:
            for col in row:
                output += str(col) + "\t"
            output += "\n"
        return output

    def recursive_backtrack(self, current_node: Node) -> None:
        current_index = self.nodes.index(current_node)
        adjacent_node_indexes = []
        for row_index in range(len(self.node_grid)):
            for col_index in range(len(self.node_grid[row_index])):
                if self.node_grid[row_index][col_index] == current_index:
                    if row_index > 0:
                        adjacent_node_indexes.append(self.node_grid[row_index - 1][col_index])
                    if row_index < len(self.node_grid) - 1:
                        adjacent_node_indexes.append(self.node_grid[row_index + 1][col_index])
                    if col_index > 0:
                        adjacent_node_indexes.append(self.node_grid[row_index][col_index - 1])
                    if col_index < len(self.node_grid) - 1:
                        adjacent_node_indexes.append(self.node_grid[row_index][col_index + 1])
        while len(adjacent_node_indexes) > 0:
            random_index = random.choice(adjacent_node_indexes)
            random_node = self.nodes[random_index]
            if not random_node.visited:
                self.adjacency_matrix[current_index][random_index] = 1
                self.adjacency_matrix[random_index][current_index] = 1
                random_node.visited = True
                self.recursive_backtrack(random_node)
            adjacent_node_indexes.remove(random_index)


my_maze_size = 20
my_maze_node_pixel_size = 20
my_maze = Graph(my_maze_size)
window = tkinter.Tk()
window.title("Maze Program")
canvas = tkinter.Canvas(window, width=(my_maze_node_pixel_size * my_maze_size * 3),
                        height=(my_maze_node_pixel_size * my_maze_size * 3))
# MAZE DRAWING GOES HERE

canvas.pack()
window.mainloop()
