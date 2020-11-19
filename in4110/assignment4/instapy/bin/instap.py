#!/usr/bin/env python3
import argparse
import os.path
from instapy.instapy_api import grayscale_image, sepia_image

def run(args):
    """
    Processes provided arguments and applies relevant functions.
    Args:
        args (argparse.Namespace): arguments provided to the script.
    Returns:
        None.
    """
    if os.path.exists(args.file):
        img_filter = grayscale_image if args.gray is not None else sepia_image
        img_filter(args.file, args.out, args.implement, args.scale)
    else:
        print('Input file does not exist. Provide a path to an image file.')

    print('Done.')


def main():
    """
    Commandline interface
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='The script applies gray or sepia filter to an image '
                                                 'and saves the result to a file on your computer.')
    parser.add_argument('-f', '--file', help='Path to input file (image only)', type=str, required=True)
    parser.add_argument("-i", "--implement", help="Select the processing mode: python, numpy, numba, cython", type=str,
                        default='numpy', choices=['python', 'numpy', 'numba', 'cython'])
    parser.add_argument('-o', '--out', help='Path to output file', type=str, required=True)
    parser.add_argument("-sc", "--scale", help="You can rescale the image. Choose a value between 0 and 1", action = "store", type=float, default = 1)
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--sepia", help="Using the sepia filter (cannot choose this alongside the greyscale filter)", action = "store_true", default = False)
    group.add_argument("-g", "--grey", help="Using the greyscale filter (cannot choose this alongside the greyscale filter)", action = "store_true", default = False)
    
    parser.set_defaults(func=run)
    args = parser.parse_args()
    
    if(args.scale <= 0 or args.scale > 1):
    	raise Exception("Invalid scale of image. Must be between 0 and 1")
    
    args.func(args)

