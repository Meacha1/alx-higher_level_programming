#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix =  [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[i]), 1):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return (new_matrix)
