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
            if current == end:
                # MISSING PATH CODE GOES HERE
                pass
            current_node_index = self.nodes.index(current)
            for col_index in range(len(self.nodes)):
                if self.adjacency_matrix[current_node_index][col_index] == 1:
                    adjacent_node = self.nodes[col_index]
                    new_score = current.score + 1
                    if new_score < adjacent_node.score:
                        adjacent_node.score = new_score
                        adjacent_node.parent = current
                        index_to_add = 0
                        for index_to_add in range(len(later_list)):
                            if later_list[index_to_add].score > adjacent_node.score:
                                break
                        later_list.insert(index_to_add, adjacent_node)


dijkstra_graph = Graph(4)
path = dijkstra_graph.dijkstra(0, 15)
