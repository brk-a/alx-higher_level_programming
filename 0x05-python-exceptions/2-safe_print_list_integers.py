#!/usr/bin/python3

"""
Docstring goes here

"""


def safe_print_list_integers(my_list=[], x=0):
    my_list = my_list if my_list and type(my_list) == list else []
    i = 0
    for j in range(x):
        try:
            if type(my_list[j]) == int:
                print('{:d}'.format(my_list[j]), end='')
                i += 1
        except (AttributeError, IndexError, TypeError, ValueError):
            pass
    print()
    return i


if __name__ == '__main__':
    safe_print_list_integers = \
        __import__('2-safe_print_list_integers').safe_print_list_integers

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
