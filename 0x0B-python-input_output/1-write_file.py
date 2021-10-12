#!/usr/bin/python3

'''
docstring goes here

'''


def write_file(filename="", text=""):
    ''' write_file fn '''
    ch_count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        ch_count += f.write(text)
    return ch_count


if __name__ == '__main__':
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_f_file.txt", "This School is so cool!\n")
    print(nb_characters)
