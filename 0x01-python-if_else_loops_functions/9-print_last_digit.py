#!/usr/bin/python3


def print_last_digit(number):
    str_num = str(number)
    last_digit = int(str_num[-1])
    print('{:d}'.format(last_digit), end='')
    return last_digit

if __name__ == '__main__':
    print_last_digit(98)
