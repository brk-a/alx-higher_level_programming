#!/usr/bin/python3


"""
class Square
defines a square by: (based on 3-square.py)

"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """__init___"""
        self.size = size

    def area(self):
        """area"""
        return self.__size * self.__size

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, val):
        """size setter"""
        if type(val) != int:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val


if __name__ == '__main__':
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
