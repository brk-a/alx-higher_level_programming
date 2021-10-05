#!/usr/bin/python3


'''
Docstring goes here

'''

import numpy as np


class Matrix:
    '''class matrix'''
    name = None

    @classmethod
    def set_name(cls, name, matrix):
        '''set_name method'''
        cls.name = name
        return cls(matrix)

    def __init__(self, matrix):
        '''__init__'''
        self.matrix = matrix

    @property
    def matrix(self):
        '''matrix property'''
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        '''matrix setter'''
        if not isinstance(matrix, list):
            raise TypeError(f'{Matrix.name} must be a list')
        if len(matrix) == 0:
            raise ValueError(f"{Matrix.name} can't be empty")
        row = len(matrix)
        col = len(matrix[0])
        if col == 0:
            raise ValueError(f"{Matrix.name} can't be empty")
        for i in range(row):
            if not type(matrix[i]) == list:
                raise TypeError(f'{Matrix.name} must be a list of lists')
        for i in range(row):
            for j in range(col):
                elem = matrix[i][j]
                if not isinstance(elem, int) and not isinstance(elem, float):
                    raise TypeError(f'{Matrix.name} should contain only integers or floats')

        self.__matrix = np.array(matrix)

    def __len__(self):
        '''len of object Matrix'''
        return len(self.__matrix)

    def __getitem__(self, index):
        '''indexing feature'''
        return self.__matrix[index]



def lazy_matrix_mul(m_a, m_b):
    '''matrix_mul'''
    m_a = m_a if m_a and type(m_a) == list else None
    m_b = m_b if m_b and type(m_b) == list else None

    m_a = Matrix.set_name('m_a', m_a)
    m_b = Matrix.set_name('m_b', m_b)

    new_m = np.matmul(m_a, m_b)
    return new_m


if __name__ == '__main__':
    lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
