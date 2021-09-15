#!/usr/bin/python3


"""
Docstring goes here

"""


def search_replace(my_list, search, replace):
    my_list = my_list if my_list and type(my_list) == list else []
    new_list = [replace if my_list[i] == search else my_list[i] for i, n in enumerate(my_list)]
    return new_list


if __name__ == '__main__':
    my_list = ['cheeky', 'chimey', 'chunky', 'chutney']
    search = 'chimey'
    replace = 'chilli'
    print(search_replace(my_list, search, replace))
    print(my_list)
