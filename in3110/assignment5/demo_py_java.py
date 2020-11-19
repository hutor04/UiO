#!/usr/bin/env python3
from highlighter import highlighter


def demo_py_java():
    print('=' * 40)
    print('Demo of Python highlighting, Theme 1.')
    print('=' * 40)
    print(highlighter('./themes/python.syntax', './themes/python.theme', './examples/coloring_example.py'))
    print('='* 40)
    print('Demo of Python highlighting, Theme 2.')
    print('=' * 40)
    print(highlighter('./themes/python.syntax', './themes/python.theme', './examples/coloring_example.py'))
    print('=' * 40)
    print('Demo of Java highlighting')
    print('=' * 40)
    print(highlighter('./themes/java.syntax', './themes/java.theme', './examples/coloring_example.java'))


if __name__ == '__main__':
    demo_py_java()
