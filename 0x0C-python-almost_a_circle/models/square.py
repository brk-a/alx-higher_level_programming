#!/usr/bin/python3

'''
Docstring goes here

'''

from rectangle import Rectangle


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
        return self.width

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

    def to_dictionary(self):
        ''' to_dict methode '''
        a = ['id', 'size', 'x', 'y']
        b = [getattr(self, attr) for attr in a]
        return {k:v for k, v in zip(a, b)}


if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
