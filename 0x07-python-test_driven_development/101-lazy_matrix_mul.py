#!/usr/bin/python3


'''
Docstring goes here

'''

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''matrix_mul'''
    m_a = m_a if m_a and type(m_a) == list else []
    m_b = m_b if m_b and type(m_b) == list else []

    new_m = np.matmul(m_a, m_b)
    return new_m


if __name__ == '__main__':
    lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
