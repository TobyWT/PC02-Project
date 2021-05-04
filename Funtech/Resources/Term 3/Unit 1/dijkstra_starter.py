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



dijkstra_graph = Graph(6)
path = dijkstra_graph.dijkstra(4, 30)
