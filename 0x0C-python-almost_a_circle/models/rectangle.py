#!/usr/bin/python3

'''
Docstring goes here

'''

from models.base import Base


class Rectangle(Base):
    ''' class Rectangle. Inherits from class Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' __init__ method '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

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

    def display(self):
        ''' represent rect using '#' '''
        rows = self.height
        cols = self.width
        for _ in range(self.y):
            print()
        for i in range(rows):
            print(' ' * self.x, end='')
            for j in range(cols):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        ''' update method '''
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        ''' to_dict method '''
        a = ['id', 'width', 'height', 'x', 'y']
        b = [getattr(self, attr) for attr in a]
        return {k: v for k, v in zip(a, b)}


if __name__ == '__main__':
    pass
