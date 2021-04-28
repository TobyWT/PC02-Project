class Node:
    def __init__(self, x: int, y: int):
        self.score = (2 ** 32) - 1
        self.distance_to_end = (2 ** 32) - 1
        self.parent = None
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)


class Graph:
    def __init__(self, square_grid_size: int):
        self.nodes = []
        for counter in range(square_grid_size * square_grid_size):
            x = counter % square_grid_size
            y = int(counter / square_grid_size)
            self.nodes.append(Node(x, y))
        self.adjacency_matrix = []
        for row_counter in range(len(self.nodes)):
            row = []
            for col_counter in range(len(self.nodes)):
                row.append(0)
            self.adjacency_matrix.append(row)
        for node_index in range(len(self.nodes)):
            if node_index / square_grid_size >= 1:
                self.adjacency_matrix[node_index][node_index - square_grid_size] = 1
            if node_index % square_grid_size != 0:
                self.adjacency_matrix[node_index][node_index - 1] = 1
            if node_index / square_grid_size < square_grid_size - 1:
                self.adjacency_matrix[node_index][node_index + square_grid_size] = 1
            if node_index % square_grid_size != square_grid_size - 1:
                self.adjacency_matrix[node_index][node_index + 1] = 1

    def a_star(self, start_index: int, end_index: int) -> [Node]:
        start = self.nodes[start_index]
        start.score = 0
        end = self.nodes[end_index]
        later_list = [start]
        while len(later_list) > 0:
            current = later_list.pop(0)
            current_node_index = self.nodes.index(current)
            if current == end:
                final_path = [end]
                path_tracker = end
                while path_tracker.parent is not None:
                    final_path.insert(0, path_tracker.parent)
                    path_tracker = path_tracker.parent
                return final_path
            for col_index in range(len(self.nodes)):
                if self.adjacency_matrix[current_node_index][col_index] == 1:
                    # MISSING CODE HERE: Calculate the correct score for the adjacent Node and update accordingly
                    pass


a_star_graph = Graph(10)
path = a_star_graph.a_star(2, 80)
for node in path:
    print(node)
