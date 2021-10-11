#!/usr/bin/python3

'''
Docstring goes here

'''


def add_attribute(obj, attr, val):
    ''' add an attr, if possible. '''
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, val)
    else:
        raise TypeError(f"can't add new attribute")


if __name__ == '__main__':
    add_attribute = __import__('101-add_attribute').add_attribute

    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
