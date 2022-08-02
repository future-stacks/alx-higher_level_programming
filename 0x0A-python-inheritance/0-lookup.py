#!/usr/bin/python3
"""
 A module: Defines a lookup function
"""

def lookup(obj):
    """
    Args: 
        obj: instance of a class

    Returns:
        (list): the list of available attributes
 and methods of an object
    """
    return dir(obj)
