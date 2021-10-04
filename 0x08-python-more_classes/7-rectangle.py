#!/usr/bin/python3

'''
Docstring goes here

'''


class Rectangle:
    ''' class Rectangle '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' __init__ '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                my_str += str(self.print_symbol)
            my_str += '\n'
        my_str += str(self.print_symbol) * self.width
        return my_str

    def __repr__(self):
        ''' __repr__ '''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        ''' __del__ '''
        print(f'Bye rectangle...')
        Rectangle.number_of_instances -= 1


if __name__ == '__main__':
    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")
