class Node:
    def __init__(self, x: int, y: int):
        self.score = (2 ** 32) - 1
        self.parent = None
        self.x = x
        self.y = y


class Graph:
    def __init__(self, square_grid_size: int):
        # Construct the __nodes list with square_grid_size**2 the number of Nodes
        self.nodes = []
        for counter in range(square_grid_size * square_grid_size):
            # Calculate the position for this Node
            x = counter % square_grid_size
            y = int(counter / square_grid_size)
            self.nodes.append(Node(x, y))

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

    # Define the A* function that returns a path between the two selected Nodes
    def a_star(self, start_index: int, end_index: int) -> [Node]:
        # Setup the starting variables for the start/end Nodes and the later list
        start = self.nodes[start_index]
        start.score = 0
        end = self.nodes[end_index]
        later_list = [start]

        # Continue iterating the algorithm while there are Nodes left to examine in the later list
        while len(later_list) > 0:
            # Pop and store the first Node as the current
            current = later_list.pop(0)
            current_node_index = self.nodes.index(current)

            # Check if the current is the end (and return the path from the start to the end if it is)
            if current == end:
                final_path = [end]
                path_tracker = end
                while path_tracker.parent is not None:
                    final_path.insert(0, path_tracker.parent)
                    path_tracker = path_tracker.parent
                return final_path


a_star_graph = Graph(10)
path = a_star_graph.a_star(2, 80)
