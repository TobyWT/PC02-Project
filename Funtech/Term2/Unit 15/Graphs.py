class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_matrix = []    # self.adjacency_matrix[x][y] <- 1 : x, y connected
        # self.adjacency_matrix = []  # self.adjacency_matrix[x][z] <- 0 : x, z NOT connected
        # self.adjacency_matrix = []  # self.adjacency_matrix[y][z] <- 1 : y, z connected
        for row in range(len(self.nodes)):
            matrix_row = []
            for column in range(len(self.nodes)):
                matrix_row.append(0)
            self.adjacency_matrix.append(matrix_row)

    def add_edge(self, row, column):
        self.adjacency_matrix[row][column] = 1
        self.adjacency_matrix[column][row] = 1


