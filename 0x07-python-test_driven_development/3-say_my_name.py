#!/usr/bin/python3

'''
Docstring goes here

'''


def say_my_name(first_name, last_name=""):
    '''say me name'''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('second_name must be a string')
    print(f'My name is {first_name} {last_name}')


if __name__ == '__main__':
    say_my_name = __import__('3-say_my_name').say_my_name

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
