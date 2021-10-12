#!/usr/bin/python3

'''
Docstring goes here

'''


def my_f(x):
    ''' factorial: x! '''
    if x == 0:
        return 1
    return x * my_f(x - 1)


def my_combos(a):
    ''' combinations: nCr '''
    li = [int(my_f(a) / (my_f(r) * my_f(a - r))) for r in range(a + 1)]
    return li


def pascal_triangle(n):
    ''' pascal_triangle '''
    if n <= 0:
        print(f'[]')
    else:
        for i in range(n):
            print(my_combos(i))


if __name__ == '__main__':
    pascal_triangle(5)
