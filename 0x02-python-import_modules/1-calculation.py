#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
    import calculator_1 as calc

    a = 10
    b = 5

    for i in dir(calc):
        if i == 'add':
            print('{:d} + {:d} = {:d}'.format(a, b, calc.add(a, b)))
        elif i == 'sub':
            print('{:d} - {:d} = {:d}'.format(a, b, calc.sub(a, b)))
        elif i == 'mul':
            print('{:d} * {:d} = {:d}'.format(a, b, calc.mul(a, b)))
        elif i == 'div':
            print('{:d} / {:d} = {:d}'.format(a, b, calc.div(a, b)))
        else:
            continue
