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
        self.__width = width

    @height.setter
    def height(self, height):
        ''' height setter '''
        self.__height = height

    @x.setter
    def x(self, x):
        ''' x setter '''
        self.__x = x

    @y.setter
    def y(self, y):
        ''' y setter '''
        self.__y = y


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
