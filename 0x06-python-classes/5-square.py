#!/usr/bin/python3


"""
class Square
defines a square by: (based on 4-square.py)

"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """__init__"""
        self.size = size

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """my_print"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            print()

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
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

    my_square.size = -89
    my_square.my_print()
