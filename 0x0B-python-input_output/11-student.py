#!/usr/bin/python3

'''
docstring goes here

'''


class Student:
    ''' class Student '''
    def __init__(self, first_name, last_name, age):
        ''' __init__ method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' to_json method '''
        obj = self.__dict__
        if not attrs:
            return obj
        else:
            new_di = {}
            for i in attrs:
                if hasattr(self, i):
                    new_di[i] = obj[i]
            return new_di

    def reload_from_json(self, json):
        ''' reload_from_json method '''
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)


if __name__ == '__main__':
    print(f' Usage: ./11-student.py <*args>')
