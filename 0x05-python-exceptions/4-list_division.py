#!/usr/bin/python3

"""
Docstring goes here

"""


def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = my_list_1 if my_list_1 and type(my_list_1) == list else []
    my_list_2 = my_list_2 if my_list_2 and type(my_list_2) == list else []

    try:
        new_li = [my_list_1[i] / my_list_2[i] for i in range(list_length)]
    except (IndexError, TypeError, ValueError, ZeroDivisionError)\
           as ide, tye, vle, zde:
        new_li.append(0)
        if zde:
            print(f'division by 0')
        if tye or vle:
            print(f'wrong type')
        if ide:
            print(f'out of range')
    except AttributeError:
        print(f'out of range')
    finally:
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
