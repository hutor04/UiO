#!/usr/bin/env python3
from diff import diff


def demo_diff():
    print('=' * 40)
    print('Demo for Diff.py')
    print('=' * 40)
    print('Original file:')
    with open('./examples/diffone.txt', 'r') as input:
        print(input.read())
    print('Edited file:')
    with open('./examples/difftwo.txt', 'r') as input:
        print(input.read())
    print('Difference file:')
    diff('./examples/diffone.txt', './examples/difftwo.txt')


if __name__ == '__main__':
    demo_diff()