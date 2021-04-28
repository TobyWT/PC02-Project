import random


class Node:
    def __init__(self, x: int, y: int):
        self.visited = False
        self.score = (2 ** 32) - 1
        self.distance_to_end = (2 ** 32) - 1
        self.parent = None
        self.x = x
        self.y = y


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

    def solve_dijkstra(self):
        pass
        # Create the start and end Nodes from the self.nodes list

        # Set the start Node's score to 0

        # Create the later list

        # Continue iterating while the later list has Nodes to examine

            # Get the first Node in the later list as the current (removing it from the list)

            # If the current Node is the end, backtrack through the parents and return the list of all those Nodes

            # Get the index of the current Node

            # Loop through all the Nodes in the self.nodes list

                # If the current Node and the iterated Node are adjacent, calculate a new score for the adjacent Node

                    # If the new score is less than the adjacent Node's current score, update it and their parent
                    # Then add the adjacent Node to the later list in the correct spot (lowest score first)

    def solve_a_star(self):
        pass
        # Create the start and end Nodes from the self.nodes list

        # Set the start Node's score to 0

        # Create the later list

        # Continue iterating while the later list has Nodes to examine

            # Get the first Node in the later list as the current (removing it from the list)

            # If the current Node is the end, backtrack through the parents and return the list of all those Nodes

            # Loop through all the Nodes in the self.nodes list

                # If the current Node and the iterated Node are adjacent, calculate a new score for the adjacent Node

                    # Do this by getting the distance from the start and the distance to the end

                    # Sum those distances to get the new score

                    # If the new score is less than the adjacent Node's current score, update
                    # their score, distance_to_end, and parent
                    # Then add the adjacent Node to the later list in the correct spot (lowest score first)

