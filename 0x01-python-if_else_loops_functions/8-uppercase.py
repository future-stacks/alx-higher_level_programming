#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 123:
            result += chr(ord(char) - 32)
        else:
            result += chr(ord(char))
    print("{}".format(result))
