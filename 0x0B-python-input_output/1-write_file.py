#!/usr/bin/python3

"""
    A module: Function that writes to file
""""


def write_file(filename="", text=""):
    """
    Writes string to a file in UTF8 format

    Args:
        filename (str): name of filename
        text (str): text to be written to file

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
