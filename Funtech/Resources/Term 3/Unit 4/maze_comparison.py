import random
import time
import tkinter


class Node:
    def __init__(self, x: int, y: int):
        self.visited = False
        self.score = (2 ** 32) - 1
        self.distance_to_end = (2 ** 32) - 1
        self.parent = None
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {}) - {}".format(self.y, self.x, self.score)


class Graph:
    def __init__(self, maze_size: int):
        self.maze_size = maze_size
        self.nodes = []
        for row_count in range(maze_size):
            for col_count in range(maze_size):
                self.nodes.append(Node(col_count, row_count))
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
        self.found_path = None

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

    def solve_dijkstra(self, later_list: [Node], end: Node, canvas: tkinter.Canvas,
                       node_square_grid, scale_size: int) -> [Node]:
        # Complete a single iteration in the algorithm
        current = later_list.pop(0)
        if current == end:
            final_path = [end]
            path_tracker = end
            while path_tracker.parent is not None:
                final_path.insert(0, path_tracker.parent)
                path_tracker = path_tracker.parent
            self.found_path = final_path
            canvas.after(1000, lambda: self.draw_path(canvas, scale_size))
            return
        current_node_index = self.nodes.index(current)
        for col_index in range(len(self.nodes)):
            if self.adjacency_matrix[current_node_index][col_index] == 1:
                adjacent_node = self.nodes[col_index]
                new_score = current.score + 1
                if new_score < adjacent_node.score:
                    adjacent_node.score = new_score
                    adjacent_node.parent = current
                    index_to_add = 0
                    while index_to_add < len(later_list):
                        if later_list[index_to_add].score > adjacent_node.score:
                            break
                        index_to_add += 1
                    later_list.insert(index_to_add, adjacent_node)

        # Edit the squares on the Canvas
        for node in later_list:
            canvas.itemconfig(node_square_grid[node.y][node.x], fill="#00AAFF")
        canvas.itemconfig(node_square_grid[current.y][current.x], fill="#FFAA00")

        # Move onto the next iteration
        canvas.after(50, lambda: self.solve_dijkstra(later_list, end, canvas, node_square_grid, scale_size))

    def solve_a_star(self, later_list: [Node], end: Node, canvas: tkinter.Canvas,
                     node_square_grid, scale_size: int) -> [Node]:
        current = later_list.pop(0)
        if current == end:
            final_path = [end]
            path_tracker = end
            while path_tracker.parent is not None:
                final_path.insert(0, path_tracker.parent)
                path_tracker = path_tracker.parent
            self.found_path = final_path
            canvas.after(1000, lambda: self.draw_path(canvas, scale_size))
            return
        current_node_index = self.nodes.index(current)
        for col_index in range(len(self.nodes)):
            if self.adjacency_matrix[current_node_index][col_index] == 1:
                adjacent_node = self.nodes[col_index]
                end_horizontal_distance = abs(end.x - adjacent_node.x)
                end_vertical_distance = abs(end.y - adjacent_node.y)
                distance_to_end = end_horizontal_distance + end_vertical_distance
                new_score = current.score + 1
                if new_score + distance_to_end < adjacent_node.score + adjacent_node.distance_to_end:
                    adjacent_node.score = new_score
                    adjacent_node.distance_to_end = distance_to_end
                    adjacent_node.parent = current
                    index_to_add = 0
                    while index_to_add < len(later_list):
                        if later_list[index_to_add].score + later_list[index_to_add].distance_to_end > adjacent_node.score + adjacent_node.distance_to_end:
                            break
                        index_to_add += 1
                    later_list.insert(index_to_add, adjacent_node)

        # Edit the squares on the Canvas
        for node in later_list:
            canvas.itemconfig(node_square_grid[node.y][node.x], fill="#00AAFF")
        canvas.itemconfig(node_square_grid[current.y][current.x], fill="#FFAA00")

        # Move onto the next iteration
        canvas.after(50, lambda: self.solve_a_star(later_list, end, canvas, node_square_grid, scale_size))

    def draw_path(self, canvas, scale_size):
        # ADD CODE TO DRAW THE PATH HERE
        pass


class MazeSolvingProgram:
    def __init__(self, maze_size, scale_size):
        # Prepare the two mazes and the tkinter GUI elements
        self.__maze_size = maze_size
        self.__scale_size = scale_size
        start_time = time.time()
        random.seed(start_time)
        self.__dijkstra_graph = Graph(maze_size)
        random.seed(start_time)
        self.__a_star_graph = Graph(maze_size)
        scaled_size = maze_size * scale_size * 3
        self.__window = tkinter.Tk()
        self.__window.title("Maze Solving Comparison")
        dijkstra_frame = tkinter.Frame(self.__window)
        dijkstra_label = tkinter.Label(dijkstra_frame, text="Dijkstra", font=("Calibri", 22))
        dijkstra_label.pack()
        self.__dijkstra_canvas = tkinter.Canvas(dijkstra_frame, width=scaled_size, height=scaled_size)
        self.__dijkstra_canvas.pack()
        a_star_frame = tkinter.Frame(self.__window)
        a_star_label = tkinter.Label(a_star_frame, text="A*", font=("Calibri", 22))
        a_star_label.pack()
        self.__a_star_canvas = tkinter.Canvas(a_star_frame, width=scaled_size, height=scaled_size)
        self.__a_star_canvas.pack(side=tkinter.LEFT)
        dijkstra_frame.pack(side=tkinter.LEFT)
        a_star_frame.pack(side=tkinter.LEFT)
        dijkstra_square_grid = self.draw_maze(self.__dijkstra_graph, self.__dijkstra_canvas)
        a_star_square_grid = self.draw_maze(self.__a_star_graph, self.__a_star_canvas)
        self.__dijkstra_canvas.after(1000, lambda: self.solve(True, self.__dijkstra_graph, self.__dijkstra_canvas, dijkstra_square_grid))
        self.__a_star_canvas.after(1000, lambda: self.solve(False, self.__a_star_graph, self.__a_star_canvas, a_star_square_grid))
        self.__window.mainloop()

    def draw_maze(self, maze: Graph, canvas: tkinter.Canvas):
        # Draw the complete maze for one graph (i.e. Dijkstra *or* A*)
        # Create a 2D list of all the rectangles (pixels) drawn for the maze)
        node_square_grid = []
        for node_row in range(self.__maze_size):
            row = []
            for node_col in range(self.__maze_size):
                for pixel_row in range(-1, 2):
                    for pixel_col in range(-1, 2):
                        if pixel_row == 0 and pixel_col == 0:
                            colour = "#FFFFFF"
                        elif (pixel_row == pixel_col
                              or (pixel_row == -1 and pixel_col == 1)
                              or (pixel_row == 1 and pixel_col == -1)):
                            colour = "#000000"
                        elif (node_row + pixel_row < 0 or node_row + pixel_row >= self.__maze_size
                              or node_col + pixel_col < 0 or node_col + pixel_col >= self.__maze_size):
                            colour = "#000000"
                        else:
                            current_node_index = maze.node_grid[node_row][node_col]
                            adjacent_node_index = maze.node_grid[node_row + pixel_row][node_col + pixel_col]
                            if maze.adjacency_matrix[current_node_index][adjacent_node_index] == 0:
                                colour = "#000000"
                            else:
                                colour = "#FFFFFF"
                        if pixel_row == 0 and pixel_col == 0:
                            row.append(canvas.create_rectangle(((node_col * 3) + pixel_col + 1) * self.__scale_size,
                                                ((node_row * 3) + pixel_row + 1) * self.__scale_size,
                                                ((node_col * 3) + pixel_col + 2) * self.__scale_size,
                                                ((node_row * 3) + pixel_row + 2) * self.__scale_size, fill=colour))
                        else:
                            canvas.create_rectangle(((node_col * 3) + pixel_col + 1) * self.__scale_size,
                                                     ((node_row * 3) + pixel_row + 1) * self.__scale_size,
                                                     ((node_col * 3) + pixel_col + 2) * self.__scale_size,
                                                     ((node_row * 3) + pixel_row + 2) * self.__scale_size, fill=colour)
            node_square_grid.append(row)
        return node_square_grid

    def solve(self, is_dijkstra: bool, maze: Graph, canvas: tkinter.Canvas, node_square_grid) -> None:
        # Start solving a specific maze (Dijkstra *or* A*)
        maze.nodes[0].score = 0
        later_list = [maze.nodes[0]]
        # Check which algorithm we're running
        if is_dijkstra:
            maze.solve_dijkstra(later_list, maze.nodes[-1], canvas, node_square_grid, self.__scale_size)
        else:
            maze.nodes[0].distance_to_end = abs(maze.nodes[-1].x - maze.nodes[0].x) + \
                                            abs(maze.nodes[-1].y - maze.nodes[0].y)
            maze.solve_a_star(later_list, maze.nodes[-1], canvas, node_square_grid, self.__scale_size)


MazeSolvingProgram(20, 10)
