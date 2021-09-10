#!/usr/bin/python3

"""
Docstring goes here

"""


def divisible_by_2(my_list=[]):
    li = [True if i % 2 == 0 else False for i in range(len(my_list))]
    return li

if __name__ == '__main__':
    my_list = [i for i in range(101)]
    print(divisible_by_2(my_list))
