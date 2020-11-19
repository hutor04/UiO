#!/usr/bin/env python3
import re
import argparse
from typing import List


def find_matches(regex_file: List, text_file: List, highlight: bool) -> None:
    """
    Grep like utility. It takes a filename and prints all lines where there the regex matches on one part of the line.
    :param regex_file: List
                    List of strings generated from the regex input file.
    :param text_file: List
                    List of strinsg generated from the text input file.
    :param highlight: bool
                    Set to True for match highlighting.
    :return: None
    """
    regex = [re.compile(line.rstrip()) for line in regex_file]
    colours = ['0;31', '0;32', '0;33']
    current_colour = 0
    matched_lines = []

    #  Loop through the list of expressions
    for pattern in regex:
        #  Loop through each line in the input
        for line in range(len(text_file)):
            matches = list(pattern.finditer(text_file[line]))

            #  Add the line to printed lines
            if len(matches) > 0:
                matched_lines.append(line)

            #  Highlight matches
            if highlight:
                for match in matches:
                    coloured_text = f'\033[{colours[current_colour]}m{match.group()}\1\033[0m'
                    text_file[line] = re.sub(pattern, coloured_text, text_file[line])

        #  Reset current colour
        if current_colour > len(colours) - 1:
            current_colour = 0
        else:
            current_colour += 1

    for i in matched_lines:
        print(text_file[i].rstrip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='Path to a source file.', default='./examples/greptext.txt')
    parser.add_argument('regex', nargs="*", type=str, help='Regular expression')
    parser.add_argument('--highlight', action='store_true', help='Use the flag to highlight the exact matches')
    args = parser.parse_args()

    try:
        with open(args.source) as source_file:
            source = source_file.readlines()
        find_matches(args.regex, source, args.highlight)
    except FileNotFoundError:
        print("File not found!")