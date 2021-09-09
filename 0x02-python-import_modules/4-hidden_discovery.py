#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
    import hidden_4

    li = [i for i in dir(hidden_4) if not i.startswith('__')]
    li.sort()
    for i in li:
        print('{:s}'.format(i))
