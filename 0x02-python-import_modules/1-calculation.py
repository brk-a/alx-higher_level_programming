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
            print(f'{a} + {b} = {calc.add(a, b)}')
        elif i == 'sub':
            print(f'{a} - {b} = {calc.sub(a, b)}')
        elif i == 'mul':
            print(f'{a} * {b} = {calc.mul(a, b)}')
        elif i == 'div':
            print(f'{a} / {b} = {calc.div(a, b)}')
        else:
            continue
