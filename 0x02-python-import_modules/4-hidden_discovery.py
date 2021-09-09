#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
    import hidden4

    li = [i for i in dir(hidden4) if not i.startswith('__')]
    for i in li:
        print('{:s}'.format(i))
