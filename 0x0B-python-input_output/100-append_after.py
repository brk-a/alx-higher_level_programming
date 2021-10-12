#!/usr/bin/python3

'''
Docstring goes here

'''


def append_after(filename="", search_string="", new_string=""):
    ''' append_after fn'''
    new_lines = []
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line)


if __name__ == '__main__':
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
