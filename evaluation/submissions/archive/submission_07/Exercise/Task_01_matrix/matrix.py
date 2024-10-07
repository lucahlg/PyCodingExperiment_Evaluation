class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, row.split())) for row in matrix_string.strip().split('\n')]

    def row(self, index):
        return self.matrix[index - 1]
        pass

    def column(self, index):
        return [self.matrix[row][index - 1] for row in range(len(self.matrix))]
        pass
