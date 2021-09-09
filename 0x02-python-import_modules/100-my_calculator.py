#!/usr/bin/python3


"""
BYOC: Build Yer [not quite] Own Calculator

A basic calculator, written in py.

Ops: add, sub, mul and div.

"""

if __name__ == '__main__':
    import sys
    import calculator_1 as calc

    num_of_args = len(sys.argv[1:])

    operators = {
        '+': calc.add,
        '-': calc.sub,
        '*': calc.mul,
        '/': calc.div}

    def driver():
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])

        if op not in operators.keys():
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
        else:
            result = operators[op](a, b)
            print('{:d} {:s} {:d} = {:d}'.format(a, op, b, result))
            return result

    if num_of_args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        driver()
