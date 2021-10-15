#!/usr/bin/python3

'''
Docstring goes here

'''

from base import Base


class Rectangle(Base):
    ''' class Rectangle. Inherits from class Base '''
    
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' __init__ method '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @width.setter
    def width(self, width):
        ''' width setter '''
        if type(width) is not int:
            raise TypeError(f'width must be an integer')
        if width <= 0:
            raise ValueError(f'width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        ''' height setter '''
        if type(height) is not int:
            raise TypeError(f'height must be an integer')
        if height <= 0:
            raise ValueError(f'height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        ''' x setter '''
        if type(x) is not int:
            raise TypeError(f'x must be an integer')
        if x < 0:
            raise ValueError(f'x must be > 0')
        self.__x = x

    @y.setter
    def y(self, y):
        ''' y setter '''
        if type(y) is not int:
            raise TypeError(f'y must be an integer')
        if y < 0:
            raise ValueError(f'y must be > 0')
        self.__y = y

    def area(self):
        ''' area methode '''
        return self.__height * self.__width


if __name__ == '__main__':
    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
