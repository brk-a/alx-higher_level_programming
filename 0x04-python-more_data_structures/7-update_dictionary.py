#!/usr/bin/python3

"""
Docstring goes here

"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary = a_dictionary if a_dictionary \
                   and type(a_dictionary) == dict else {}
    new_dict = a_dictionary
    new_dict[key] = value
    return a_dictionary

if __name__ == '__main__':
    print_s = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_s(new_dict)
    print("--")
    print_s(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "Nairobi")
    print_s(new_dict)
    print("--")
    print_s(a_dictionary)
