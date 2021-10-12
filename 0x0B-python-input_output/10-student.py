#!/usr/bin/python3

'''
Docstring goes here

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

'''
if __name__ == '__main__':
    Student = __import__('10-student').Student

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
'''
