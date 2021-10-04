#!/usr/bin/python3

'''
Docstring goes here

'''

import unittest


def max_integer(list=[]):
    '''max_int'''
    list = list if list and type(list) == list else []
    
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


class TestMaxInteger(unittest.TestCase):

    def test_simple_complete_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 0, -1]), 4)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_simple_empty_none_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, None)

    def test_string_comparison(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 3, '4'])
        self.assertRaises(TypeError, max_integer, ['1', 2, 3, 4])
        self.assertRaises(TypeError, max_integer, [1, '2', '3', 4])

    def test_integer_comparison_none(self):
        self.assertRaises(TypeError, max_integer, [1, None, 3])


if __name__ == '__main__':
    unittest.main()
