#!/usr/bin/python3

'''
Docstring goes here

'''


class BaseGeometry:
    ''' BaseGeometry class '''
    def area(self):
        ''' area method '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' int_validator method '''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


if __name__ == '__main__':
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
