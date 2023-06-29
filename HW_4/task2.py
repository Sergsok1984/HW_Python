# 2. Напишите функцию для транспонирования матрицы.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(input_matrix):
    for column in input_matrix:
        for row in column:
            print(row, "\t", end="")
        print()


def transposition_matrix(input_matrix):
    return [list(row) for row in zip(*input_matrix)]


print_matrix(matrix)
print()
print_matrix(transposition_matrix(matrix))
