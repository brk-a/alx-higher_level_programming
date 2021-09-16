#!/usr/bin/python3

"""
Docstring goes here

"""


def complex_delete(a_dictionary, value):
    a_dictionary = a_dictionary if a_dictionary \
                   and type(a_dictionary) == dict else {}
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        new_dict = dict(a_dictionary)
        for k, v in new_dict.items():
            if v == value:
                a_dictionary.pop(k)
        return a_dictionary


if __name__ == '__main__':
    print_sorted_dictionary = \
                              __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
