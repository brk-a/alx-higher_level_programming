#!/usr/bin/python3

'''
Docstring goes here

'''


def read_file(filename=""):
    ''' read_file fn '''
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')


if __name__ == '__main__':
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")
