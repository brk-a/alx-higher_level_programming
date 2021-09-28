#!/usr/bin/python3

""""
Docstring goes here

"""


def safe_print_list(my_list=[], x=0):
    my_list = my_list if my_list and type(my_list) == list else []
    i = 0
    for j in range(x):
        try:
            print(f'{my_list[j]}', end='')
            i += 1
        except IndexError:
            break
    print()
    return i


if __name__ == '__main__':
    safe_print_list = __import__('0-safe_print_list').safe_print_list

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
