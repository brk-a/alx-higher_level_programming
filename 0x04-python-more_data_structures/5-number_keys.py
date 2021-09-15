#!/usr/bin/python3

"""
Docstring goes here

"""


def number_keys(a_dictionary):
    a_dictionary = a_dictionary if a_dictionary and type(a_dictionary) == 'dict' else {}
    keys = a_dictionary.keys()
    return len(keys)


if __name__ == '__main__':
    a_dictionary = { 'starter': "samosa", 'main': 'couscous', 'dessert': "chutney" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
