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
    return [int(my_f(a) / (my_f(r) * my_f(a - r))) for r in range(a + 1)]


def pascal_triangle(n):
    ''' pascal_triangle '''
    if n <= 0:
        print(f'[]')
    else:
        return [my_combos(i) for i in range(n)]


if __name__ == '__main__':
    pascal_triangle = __import__('12-pascal_triangle').pascal_triangle


    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))


    print_triangle(pascal_triangle(5))
