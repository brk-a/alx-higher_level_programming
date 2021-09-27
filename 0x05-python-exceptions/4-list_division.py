#!/usr/bin/python3

"""
Docstring goes here

"""


def safe_div(a, b):
    resultt = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print(f'division by 0')
    except TypeError:
        print(f'wrong type')
    finally:
        return result


def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = my_list_1 if my_list_1 and type(my_list_1) == list else []
    my_list_2 = my_list_2 if my_list_2 and type(my_list_2) == list else []

    new_li = []
    for i in range(list_length):
        try:
            new_li.append(safe_div(my_list_1[i], my_list_2[i]))
        except IndexError:
            print(f'out of range')
            new_li.append(0)

    return new_li


if __name__ == '__main__':
    list_division = __import__('4-list_division').list_division

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
