#!/usr/bin/python3


def print_last_digit(number):
    last_digit = str(number)

    print('{:d}'.format(last_digit[-1]), end='')
    return last_digit[-1]

if __name__ == '__main__':
    print_last_digit(98)
