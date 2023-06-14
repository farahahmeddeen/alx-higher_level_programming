#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mmatrix = matrix.copy()
    s = len(matrix)
    for j in range(s):
        mmatrix[j] = list(map(lambda x: x**2, matrix[j]))
    return (mmatrix)
