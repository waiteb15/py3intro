#!/usr/bin/env python
"""
Example of reading file data into a dictionary of tuples
"""
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    """
    Program entry point

    :return: none
    """
    kdata = read_data(FILE_NAME)
    prettyprint_data(kdata)
    print_fields(kdata)
    print_titles(kdata)
    print_name_and_title(kdata)
    sort_by_color(kdata)
    print_items(kdata)

def read_data(file_name):
    """
    Read data from specified file into dict.

    :param file_name: File to read
    :return: dict of data
    """
    knight_data = {}
    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            # print(name, title, color, quest, comment)
            knight_data[name] = title, color, quest, comment
    return knight_data

def prettyprint_data(data):
    """
    Pretty-print the knight data

    :param data: dict of data
    :return: None
    """
    pprint(data)

def print_fields(data):
    """
    Print some fields

    :param data: dict of data
    :return: None
    """
    print(data['Galahad'][2])
    print(data['Robin'])
    title, color, quest, comment = data['Lancelot']
    print(color, title)
    print()

def print_titles(data):
    """
    print a list of titles and names

    :param data: dict of data
    :return: None
    """
    for name, info in data.items():
        print(info[0], name)
    print()

def print_name_and_title(data):
    """
    print a list of titles and names


    :param data: dict of data
    :return: None
    """
    for name, (title, color, quest, comment) in data.items():
        print(title, name)
    print()

def by_color(k):
    """
    Key function for sorting by color

    :param k:  one key-value pair
    :return: tuple for sorting
    """
    return k[1][1], k[0]

def sort_by_color(data):
    """
    sort knights by color

    :param data: dict of data
    :return: None
    """
    for name, info in sorted(data.items(), key=by_color):
        title, color, quest, comment = info
        print(title, name, color)
    print()

def print_items(data):
    """
    print just items

    :param data: dict of data
    :return: None
    """
    print(data.items())

if __name__ == '__main__':
    main()
