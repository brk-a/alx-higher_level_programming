#!/usr/bin/python3

'''
Docstring goes here

'''

from base import Rectangle


class Square(Rectangle):
    ''' class Square. inherits from class Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' __init__ method '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.height}'

    @property
    def size(self):
        ''' size property '''
        return size.width

    @size.setter
    def size(self, size):
        ''' size setter '''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        ''' update method '''
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v
