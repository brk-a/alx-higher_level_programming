#!/usr/bin/python3

"""
Docstring goes here

"""


def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            print(*i)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print_matrix_integer(matrix)

    matrix = [[]]
    print_matrix_integer(matrix)

    matrix = [
        ['a', 'A'],
        ('b', 'B')]
    print_matrix_integer(matrix)
