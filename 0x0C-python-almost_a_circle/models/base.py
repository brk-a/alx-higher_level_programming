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
        list_dictionaries =\
            list_dictionaries if list_dictionaries and\
            type(list_dictionaries) == list else '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' methode from_json_string '''
        json_string =\
            json_string if json_string and type(json_string) == str else ''
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' methode save_to_file '''
        list_objs = list_objs if list_objs and type(list_objs) == list else []
        a = [obj.to_dictionary() for obj in list_objs]
        if len(a) > 0:
            b = Base.to_json_string(a)
        with(f'{cls.__name__}.json', 'w') as fi:
            fi.write(b)

    @classmethod
    def create(cls, **dictionary):
        ''' methode create '''
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' methode load_from_file '''
        try:
            with open(f'{cls.__name__}.json', 'r', encoding='utf-8') as fi:
                output_li = cls.from_json_string(fi.read())
                obj_li = [cls.create(**obj)) for obj in output_li]
        except Exception:
            pass
        return obj_li


if __name__ == '__main__':
    pass
