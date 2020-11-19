#!/usr/bin/env python3
from grep import find_matches

def demo_grep():
    with open('./examples/grepregex.txt', 'r') as regex_file:
        reg = regex_file.readlines()
    with open('./examples/greptext.txt', 'r') as source_file:
        source = source_file.readlines()

    print('=' * 40)
    print('Printing source file.')
    print('=' * 40)
    for line in source:
        print(line.strip())

    print('=' * 40)
    print('Printing grepped file.')
    print('Regex: hello, world, sh\w\wld')
    print('=' * 40)
    find_matches(reg, source, True)


if __name__ == '__main__':
    demo_grep()
