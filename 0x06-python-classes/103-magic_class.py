import math


class MagicClass:
    """magic class"""
    def __init__(self, radius=0):
        """__init__"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area"""
        return math.pi * pow(self.__radius, 2)

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.__radius
