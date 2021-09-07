#!/usr/bin/python3

def print_last_digit(number):
    if isnumeric(number):
        number = str(number)
        print({:d}.format(number[-1]))
    else:
        return

if __name__ ='__main__':
    print_last_digit(98)
