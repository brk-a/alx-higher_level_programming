#!/usr/bin/python3
def print_low_alpha_sans():
            for i in range(97, 123):
                        if i != 101 and i != 113:
                                    print('{}'.format(chr(i)), end='')


if __name__ == '__main__':
            print_low_alpha_sans()
