class LocationGraph:
    def __init__(self, places):
        self.places = list(places)
        self.adjacency_matrix = []
        for row in range(len(self.places)):
            matrix_row = []
            for column in range(len(self.places)):
                matrix_row.append(0)
            self.adjacency_matrix.append(matrix_row)

    def add_connection(self, row, column):
        self.adjacency_matrix[row][column] = 1
        self.adjacency_matrix[column][row] = 1
