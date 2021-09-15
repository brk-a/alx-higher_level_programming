#!/usr/bin/python3

"""
Docstring goes here

"""


def print_sorted_dictionary(a_dictionary):
    a_dictionary = a_dictionary if a_dictionary and type(a_dictionary) == dict else {}
    sort_keys = sorted(a_dictionary.keys())
    for i in sort_keys:
        print('{:s}: {}'.format(i, a_dictionary[i]))

if __name__ == '__main__':
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
