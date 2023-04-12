#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """This function adds two integers
    :para a:The first integer
    :type a: int
    :para b: The second integer whose default value is 98
    :type b: int
    :return: The addition of a and b
    :rtype: int
    :Raises: TypeError if either a or b is not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
