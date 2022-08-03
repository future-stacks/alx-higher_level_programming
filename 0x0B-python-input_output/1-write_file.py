#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes string to a file in UTF8 format

    Args:
        filename (str): name of filename
        text (str): text to be written to file

    Returns:
        int: number of characters written
    """
    with open(filename, mode='w', encoding='utf8') as file:
        return file.write(text)
