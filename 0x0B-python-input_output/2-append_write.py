#!/usr/bin/python3

'''
Docstring goes here

'''


def append_write(filename="", text=""):
    ''' append_write fn '''
    ch_count = 0
    with open(filename, 'a', encoding='utf-8') as f:
        ch_count += f.write(text)
    return ch_count


if __name__ == '__main__':
    append_write = __import__('2-append_write').append_write

    nb_chars_added = append_write("f_ap.txt", "This School is so cool!\n")
    print(nb_chars_added)
