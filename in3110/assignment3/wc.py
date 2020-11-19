#!/usr/bin/env python3

import sys
from pathlib import Path


def files_from_pattern(pattern):
    """
    Gets a pattern and searches for files that match a pattern
    :param pattern: Name of a file or mattern, e.g. 'a'
    :return: Generator over the found matches.
    """
    current_dir = Path.cwd()
    return Path(current_dir).glob(pattern)


def counter(file):
    """
    Counts the number of lines, words, and characters in a file.
    :param file: Path object
    :return: The tuple (no of lines, no of words, no of character, file name)
    """
    lines = 0
    words = 0
    characters = 0

    with open(file, 'r') as in_file:
        for line in in_file:
            lines += 1
            words += len(line.split())
            characters += len(line.rstrip('\n'))  # Strips off new line character

    return lines, words, characters, file.name


def main(args):
    """
    Unpacks the input values, checks if the input is valid: path exists, and path is a
    file. Takes arbitrary number of arguments. Wildcard strings can appear at any
    position of the input.
    :param args: The iterable with filenames or patterns
    :return: Prints out the counts.
    """
    files = []
    for i in args[1:]:
        if i.startswith('*'):
            files += [f for f in files_from_pattern(i) if f.is_file()]
        if Path(i).is_file():
            files.append(Path(i))
    if len(files) == 0:
        print('No files found matching your query.')
    else:
        for file in files:
            result = counter(file)
            print(f'{result[0]} {result[1]} {result[2]} {result[3]}')


args = sys.argv
main(args)
