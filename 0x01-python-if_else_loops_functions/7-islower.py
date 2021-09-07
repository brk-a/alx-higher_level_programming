#!/usr/bin/python3

def islower(c):
    li = [chr(i) for i in range(ord('a'), ord('z')+1)]
    if c in li:
        return True
    return False

if __name__ == '__main__':
    print(islower('A'))
