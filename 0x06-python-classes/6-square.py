#!/usr/bin/python3


"""
class Square
defines a square by: (based on 5-square.py)

"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(val[0], int) or not isinstance(val[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif val[0] < 0 or val[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = val


if __name__ == '__main__':
    Square = __import__('6-square').Square

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
