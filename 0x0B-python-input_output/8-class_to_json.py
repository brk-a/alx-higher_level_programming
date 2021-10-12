#!/usr/bin/python3

'''
Docstring goes here

'''


def class_to_json(obj):
    ''' class_to_json fn '''
    return obj.__dict__


if __name__ == '__main__':
    """ My class module
"""


    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    MyClass = __import__('8-my_class').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
