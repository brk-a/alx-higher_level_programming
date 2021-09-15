#!/usr/bin/python3

"""
Docstring goes here

"""


def best_score(a_dictionary):
    a_dictionary = a_dictionary if a_dictionary and type(a_dictionary) == dict else {}
    score = None
    person = None
    for k in a_dictionary.keys():
        if score is None or a_dictionary[k] > score:
            score = a_dictionary[k]
            person = k
    return person

if __name__ == '__main__':
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
