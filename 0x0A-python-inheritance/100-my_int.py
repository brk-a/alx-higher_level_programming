#!/usr/bin/python3

'''
docstring goes here

'''


class MyInt(int):
    ''' "Stay Taliban". class int responds viz... '''
    def __eq__(self, n2):
        ''' taliban __eq__ method '''
        return super().__ne__(n2)

    def __ne__(self, n2):
        ''' taliban __ne__ method '''
        return super().__eq__(n2)


if __name__ == '__main__':
    MyInt = __import__('100-my_int').MyInt

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
