#!/usr/bin/python3

'''
Docstring goes here

'''

import json


class Base:
    ''' class Base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' __init__ method '''
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' methodio to_json_string '''
        list_dictionaries = list_dictionaries if list_dictionaries and type(list_dictionaries) == list else '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' methodio save_to_file '''
        list_objs = list_objs if list_objs and type(list_objs) == list else []
        a = [obj.to_dictionary() for obj in list_objs]
        if len(a) > 0:
            b = Base.to_json_string(a)
        with(cls.__name__ + '.json', 'w') as f:
            f.write(b)


if __name__ == '__main__':
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
