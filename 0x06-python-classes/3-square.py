#!/usr/bin/python3

"""
class Square
defines a square by: (based on 2-square.py)

"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """__init__"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size


if __name__ == '__main__':
    Square = __import__('3-square').Square

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
