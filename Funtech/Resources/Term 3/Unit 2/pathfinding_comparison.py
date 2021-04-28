class Node:
    def __init__(self, x: int, y: int):
        self.score = (2 ** 32) - 1
        self.parent = None
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)


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

    # Resets the Nodes in the Graph so pathfinding algorithms can be reused
    def reset(self):
        for node in self.nodes:
            node.score = (2 ** 32) - 1
            node.parent = None

    # Instance function that finds a path between start/end using Dijkstra
    def dijkstra(self, start_index: int, end_index: int) -> [Node]:
        # Setup the start/end Nodes and the later list
        start = self.nodes[start_index]
        start.score = 0
        end = self.nodes[end_index]
        later_list = [start]

        # Keep repeating the algorithm while there are Nodes left in the list
        while len(later_list) > 0:

            # Pop and store the first Node in the later list as the current
            current = later_list.pop(0)

            # Check if it is the end Node (and if so return the path from it to the start Node)
            if current == end:
                final_path = [end]
                path_tracker = end
                while path_tracker.parent is not None:
                    final_path.insert(0, path_tracker.parent)
                    path_tracker = path_tracker.parent
                return final_path

            # Look through the current Node's adjacent Nodes and calculate their new score
            current_node_index = self.nodes.index(current)
            for col_index in range(len(self.nodes)):
                if self.adjacency_matrix[current_node_index][col_index] == 1:
                    adjacent_node = self.nodes[col_index]
                    new_score = current.score + 1

                    # If the new score is less than their current score, update it and set their parent to the current
                    if new_score < adjacent_node.score:
                        adjacent_node.score = new_score
                        adjacent_node.parent = current

                        # Add the adjacent Node to the later list at the correct index
                        index_to_add = 0
                        for index_to_add in range(len(later_list)):
                            if later_list[index_to_add].score > adjacent_node.score:
                                break
                        later_list.insert(index_to_add, adjacent_node)

    # A* ALGORITHM CODE GOES HERE
    def a_star(self, start_index: int, end_index: int) -> [Node]:
        pass


square_size = 100
start_node_index = 0
end_node_index = square_size - 1
print("Setting up Graph, can take a minute or more for a square size more than 100 (10,000 Nodes)")
comparison_graph = Graph(square_size)

print("Starting Dijkstra Algorithm")
dijkstra_path = comparison_graph.dijkstra(start_node_index, end_node_index)
print("Ending Dijkstra Algorithm")

print("Resetting graph...")
comparison_graph.reset()

print("Starting A* Algorithm")
a_star_path = comparison_graph.a_star(start_node_index, end_node_index)
print("Ending A* Algorithm")
