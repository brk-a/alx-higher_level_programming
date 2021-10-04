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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' bigger or equal '''
        rect_1 = rect_1 if rect_1 and isinstance(rect_1, Rectangle) else None
        rect_2 = rect_2 if rect_2 and isinstance(rect_2, Rectangle) else None

        if not isinstance(rect_1, Rectangle):
            raise TypeError(f'rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError(f'rect_2 must be an instance of Rectangle')
        if rect_2.area > rect_1.area:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        ''' square method '''
        return cls(size, size)


if __name__ == '__main__':
    Rectangle = __import__('9-rectangle').Rectangle

    my_sq = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_sq.area(), my_sq.perimeter()))
    print(my_sq)
