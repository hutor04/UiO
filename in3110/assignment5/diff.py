#!/usr/bin/env python3
import re
import argparse
import sys
from highlighter import highlighter


def diff(fileone: str, filetwo: str) -> str:
    """
    The function takes two files as input, and outputs a file containing all changes which have to be made to the first
    file to make it into the second file. The difference strings are coloured.
    :param fileone: str
                    Path to an original file.
    :param filetwo: str
                    Path to an edited file.
    :return: str
                    Outputs a string that shows the difference between two files, prints it to standard output and
                    saves to the file diff_output.txt.
    """
    syntax = './themes/diff.syntax'
    theme = './themes/diff.theme'
    output = 'diff_output.txt'

    try:
        with open(fileone, 'r') as one_input_file:
            data1 = [line.rstrip() for line in one_input_file]
    except FileNotFoundError:
        print("File 1 not found!")
        sys.exit()

    try:
        with open(filetwo, 'r')as two_input_file:
            data2 = [line.rstrip() for line in two_input_file]
    except FileNotFoundError:
        print("File 2 not found!")
        sys.exit()

    def first_element_greater_than(list, number):
        """ Returns the first element in 'list' that is greater than 'number' """
        for i in range(len(list)):
            if list[i] > number:
                return list[i]

    # The list to be printed out.
    output = data1

    # The list with same size as 'output' holding information whether lines are changed or not.
    # Each element is either 'True' or 'False' which means the line (with the same index) is changed or not.
    changed = []

    # Check deleted lines.
    for i in range(len(data1)):
        changed.append(False)
        if data1[i] not in data2:
            # Add the deleted line into 'output'
            output[i] = "- " + data1[i]
            changed[i] = True

    # Index of the latest inserted line.
    latest = 0

    # Check inserted lines.
    for i in range(len(data2)):
        line = data2[i]
        if line not in data1:
            if i == 0:
                output.insert(0, "+ " + line)
                changed.insert(0, True)
                latest = 0
            else:
                previous_line = data2[i-1]

                # Find indices of all lines (in 'output') that are equal to 'previous_line'.
                # If the previous line already exists in file 1.
                indices = [j for j, x in enumerate(output) if x == previous_line]

                # If the previous line does not exist in file 1.
                if len(indices) == 0:
                    indices = [j for j, x in enumerate(output) if x == "+ " + previous_line]

                # Find the position to add the inserted line in.
                if first_element_greater_than(indices, latest) != None:
                    latest = first_element_greater_than(indices, latest)
                
                # Add the inserted line into 'output'.
                output.insert(latest + 1, "+ " + line)
                changed.insert(latest + 1, True)

    # Add '0 ' before the lines that are not changed.
    for i in range(len(changed)):
        if not changed[i]:
            output[i] = "0 " + output[i]

    # Print to the screen and write to file.
    file = open("diff_output.txt", "w")
    for line in output:
        decoded = line.encode('ascii', 'ignore').decode("utf-8")
        print(decoded)
        file.write(f"{decoded}\n")

    file.close()

    # Apply highlighter.
    print(highlighter(syntax, theme, 'diff_output.txt'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('one', help='Path to a original file', default='./examples/diffone.txt')
    parser.add_argument('two', help='Path to an edited file.', default='./examples/difftwo.txt')
    args = parser.parse_args()
    diff(args.one, args.two)