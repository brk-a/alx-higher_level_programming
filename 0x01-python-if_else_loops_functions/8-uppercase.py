#!/usr/bin/python3

def uppercase(str):
    word = ''
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            word += chr(ord(i) - 32)
        else:
            word += i
    print('{}'.format(word))


if __name__ == '__main__':
    uppercase('holberton')
