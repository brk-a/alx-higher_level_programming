#!/usr/bin/python3

"""
my attempt at a disassembler tool

"""

import dis
import sys

def disassembler():
    arg = sys.argv[1]
    if len(sys.argv) != 2:
        print(f'Error: too many args')
        print(f'Usage: ./disassembler <file>')
        sys.exit(1)

    dis_file = dis.dis(arg)

    with open(dis_file, 'r') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    disassembler()
