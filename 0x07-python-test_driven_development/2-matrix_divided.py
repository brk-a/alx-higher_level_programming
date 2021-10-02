#!/usr/bin/python3

'''
Docstring goes here

'''


def matrix_divided(matrix, div):
    '''matrix_div'''
    matrix = matrix if matrix and type(matrix) == list else None

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError('matrix must be a matrix (list of lists)\
        of integers/floats')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if len(matrix[i]) != col:
            raise TypeError('Each row of the\
            matrix must have the same size')
    for i in range(row):
        for j in range(col):
            elem = matrix[i][j]
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError('matrix must be a\
                matrix (list of lists) of integers/floats')

    new_mx = [[float('%0.2f' % (matrix[i][j] / div)) for j in range(col)] for i in range(row)]
    return new_mx


if __name__ == '__main__':
    matrix_divided = __import__('2-matrix_divided').matrix_divided

    matrix = [
        [1, 2, 3],
        [4, 5, 6]]

    print(matrix_divided(matrix, 3))
    print(matrix)
