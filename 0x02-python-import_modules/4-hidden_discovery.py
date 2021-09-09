#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
#import marshal
    import hidden_4

#with open('hidden_4.pyc', 'rb') as h_4:
#h_4.seek(8)
#code_obj = marshal.load(h_4)
#hidden_4 = uncompyle6 -o . hidden_4.pyc

#exec(code_obj)

    li = [i for i in dir(hidden_4) if not i.startswith('__')]
    li.sort()
    for i in li:
        print('{:s}'.format(i))
