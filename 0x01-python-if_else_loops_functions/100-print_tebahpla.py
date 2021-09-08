#!/usr/bin/python3


def rev_alpha():
    counter = 0
    for i in range(122, 96, -1):
        if i % 2 == 0:
            counter = i
        else:
            counter = i - 32
        print(f"{chr(counter)}", end='')

if __name__ == '__main__':
    rev_alpha()
