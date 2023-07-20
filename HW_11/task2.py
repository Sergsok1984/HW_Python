# 1. Создайте класс Матрица. Добавьте методы для:
#    - вывода на печать,
#    - проверку на равенство,
#    - сложения,
#    - *умножения матриц.

class Matrix:

    def __init__(self, matrix: list[list[int, float]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.columns and self.rows == other.rows:
                result = [[] for _ in range(self.rows)]
                for i in range(self.rows):
                    for j in range(self.columns):
                        result[i].append(self.matrix[i][j] + other.matrix[i][j])
                return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.matrix)]
                          for self_row in self.matrix]
            elif self.rows == other.columns:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.matrix)]
                          for other_row in other.matrix]
            else:
                return "Матрицы перемножить нельзы"
            return Matrix(result)
        return False

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result = []
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.append(self.matrix[i][j] == other.matrix[i][j])
                return all(result)
        return False

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix]) + '\n'

# matr_a = Matrix([[1, 2, 2], [3, 1, 1]])
# matr_b = Matrix([[10, 6, 1], [7, 5, 5]])
# matr_c = Matrix([[4, 2], [3, 1], [1, 5]])
#
# print(matr_a)
# print(matr_c)

# print(f'{matr_a == matr_b = }')

# print(matr_a + matr_b)
# print(matr_a * matr_c)
# print(matr_a * matr_b)
