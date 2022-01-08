#!/usr/bin/python3

"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """find_peak"""
    list_of_integers = list_of_integers if list_of_integers\
        and isinstance(list_of_integers, list) else []
    
    len_lst = len(list_of_integers)

    if len_lst < 2:
        return None

    peak = list_of_integers[0]

    for i in range(1, len_lst):
        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]

    return peak

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak(["Goat_Matata", "Dada_Ng'ombe","Kaka_Mbweha"]))
    print(find_peak([1,4]))
    print(find_peak([1, 4,9]))
