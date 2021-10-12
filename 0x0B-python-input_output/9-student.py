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

    def to_json(self):
        ''' to_json method '''
        return (self.__dict__)


'''
if __name__ == '__main__':
    Student = __import__('9-student').Student

    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
'''
