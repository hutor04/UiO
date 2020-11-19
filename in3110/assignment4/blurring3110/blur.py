#!/usr/bin/env python3

import argparse
import os.path
from blurring3110.blur_1 import convert_py
from blurring3110.blur_2 import convert_np
from blurring3110.blur_3 import convert_nb

modes = [convert_py, convert_np, convert_nb]


def run(args):
    """
    Parse arguments to the respective conversion functions. Additionally checks if the input file exists,
    throws a warning if the file does not exist. Checks if the --mode argument is within the required range,
    if the argument is out of range falls back to the default mode (Python).

    :param args: argparse.Namespace
                The name space of argparser module.
    :return: None
    """

    mode = 0
    if args.mode not in [1, 2, 3]:
        print('Wrong mode input, falling back to the default mode Python (1).')
    else:
        mode = args.mode - 1

    if os.path.exists(args.input):
        modes[mode](args.input, args.out)
    else:
        print('Input file does not exist. Provide a path to an image file.')

    print('Done.')


def main():
    parser = argparse.ArgumentParser(description='The script applies blurring filter to an image '
                                                 'and saves the result to a file on your computer.'
                                                 'Provide input and output file names nad optionally select the'
                                                 'processing mode: 1 - python, 2 - numpy, 3 - numba.')
    parser.add_argument('input', help='Path to input file (image only)', type=str)
    parser.add_argument('out', help='Path to output file', type=str)
    parser.add_argument("-m", "--mode", help="Select the processing mode: 1 - python, 2 - numpy, 3 - numba.", type=int,
                        default=1)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
