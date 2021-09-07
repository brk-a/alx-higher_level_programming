#!/usr/bin/python3

def uppercase(str):
    word = ''
    for i in str:
        if i >= chr('a') and i <= chr('z'):
            word += chr(ord('i') - 32)
        else:
            word += i
    print('{}'.format(word))


if __name__ = '__main__':
    uppercase('holberton')
