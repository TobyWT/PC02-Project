import tkinter


class Node:
    def __init__(self, identifier: int):
        self.id = identifier
        self.score = (2 ** 32) - 1
        self.parent = None

    def __str__(self) -> str:
        return str(self.id)


class Graph:
    def __init__(self, size: int):
        self.nodes = []
        for count in range(size * size):
            self.nodes.append(Node(count))

        self.adjacency_matrix = []
        for row_count in range(size * size):
            row = []
            for col_count in range(size * size):
                row.append(0)
            self.adjacency_matrix.append(row)

        for row_count in range(size):
            for col_count in range(size):
                current_index = (row_count * size) + col_count
                up_index = ((row_count - 1) * size) + col_count
                down_index = ((row_count + 1) * size) + col_count
                left_index = (row_count * size) + col_count - 1
                right_index = (row_count * size) + col_count + 1
                if 0 <= row_count - 1 < size:
                    self.adjacency_matrix[current_index][up_index] = 1
                    self.adjacency_matrix[up_index][current_index] = 1
                if 0 <= row_count + 1 < size:
                    self.adjacency_matrix[current_index][down_index] = 1
                    self.adjacency_matrix[down_index][current_index] = 1
                if 0 <= col_count - 1 < size:
                    self.adjacency_matrix[current_index][left_index] = 1
                    self.adjacency_matrix[left_index][current_index] = 1
                if 0 <= col_count + 1 < size:
                    self.adjacency_matrix[current_index][right_index] = 1
                    self.adjacency_matrix[right_index][current_index] = 1
