#!/usr/bin/python3

'''
Docstring goes here

'''


class Rectangle:
    ''' class Rectangle '''
    def __init__(self, width=0, height=0):
        ''' __init__ '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width '''
        return self.__width

    @property
    def height(self):
        ''' height '''
        return self.__height

    @width.setter
    def width(self, width):
        ''' width setter '''
        if not isinstance(width, int):
            raise TypeError(f'width must be an integer')
        if width < 0:
            raise ValueError(f'width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height):
        ''' height setter '''
        if not isinstance(height, int):
            raise TypeError(f'height must be an integer')
        if height < 0:
            raise TypeError(f'height must be >= 0')
        self.__height = height

    def perimeter(self):
        ''' perimeter '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def area(self):
        ''' area '''
        return self.__height * self.__width

    def __str__(self):
        ''' __str__ '''
        my_str = ''
        if self.width == 0 or self.height == 0:
            return my_str
        for j in range(self.height - 1):
            for i in range(self.width):
                my_str += '#'
            my_str += '\n'
        my_str += '#' * self.width
        return my_str

    def __repr__(self):
        ''' __repr__ '''
        return f'Rectangle({self.width}, {self.height})'


if __name__ == '__main__':
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
