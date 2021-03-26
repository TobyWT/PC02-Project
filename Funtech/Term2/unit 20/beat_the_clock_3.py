class Graph:
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__adjacency_matrix = []
        for row in range(len(self.__nodes)):
            matrix_row = []
            for col in range(len(self.__nodes)):
                matrix_row.append(0)
            self.__adjacency_matrix.append(matrix_row)

    def add_edge(self, column, row):
        self.__adjacency_matrix[row][column] = 1
        self.__adjacency_matrix[column][row] = 1

