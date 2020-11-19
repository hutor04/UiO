#!/usr/bin/env python3
import re
import argparse
import sys


def highlighter(syntax: str, theme: str, source: str) -> str:
    """
    The function takes paths to syntax file, theme file, and source file. It applies regex rules to the sources
    file and colours it according to the rules provided by syntax file using regular expressions.
    :param syntax: string
                Path to the syntax file.
    :param theme: string
                Path to the theme file.
    :param source: string
                Path to the source file.
    :return: None
                Print the coloured string to the standard output.
    """
    syntax_rules = {}
    coloring_rules = {}
    coloured_text = ''
    separator = ': '

    #  Read syntax
    try:
        with open(syntax, 'r') as syntax_file:
            for line in syntax_file:
                elements = line.rstrip().split(separator)
                syntax_rules[elements[1]] = elements[0]
    except FileNotFoundError:
        print("Syntax file not found!")
        sys.exit()

    #  Read theme
    try:
        with open(theme, 'r') as theme_file:
            for line in theme_file:
                elements = line.rstrip().split(separator)
                coloring_rules[elements[0]] = elements[1]
    except FileNotFoundError:
        print("Theme file not found!")
        sys.exit()

    #  Read source
    try:
        with open(source, 'r') as source_file:
            input_text = source_file.read()
    except FileNotFoundError:
        print("Source file not found!")
        sys.exit()

    #  Colour a match group
    def group_coloring(matchobj) -> str:
        """
        Helper function. It is used to colour text found by match groups.
        :param matchobj: re.Match
                        Match object.
        :return: str
                    Returns as string coloured according to the rules and theme.
        """
        result = ''
        for key in matchobj.groupdict().keys():
            if key == 'wrapper' or matchobj.group(key) is None:
                continue
            result += f'\033[{coloring_rules[key]}m{matchobj.group(key)}\1\033[0m'

        return result

    #  Handle comments coloring

    c = {'block_comment', 'inline_comment', 'string'}
    if len(c - set(syntax_rules.keys())) == 0:
        comment_string_regex = syntax_rules['block_comment'] + '|' + syntax_rules['inline_comment'] + '|' + syntax_rules['string']
        comment = re.search(comment_string_regex, input_text)

        while comment is not None:
            prefix = input_text[:comment.start()]
            for key in syntax_rules.keys():
                prefix = re.sub(syntax_rules[key], group_coloring, prefix)
            coloured_text += prefix + group_coloring(comment)
            input_text = input_text[comment.end():]
            comment = re.search(comment_string_regex, input_text)

    #  Coloring the remaining part
    for key in syntax_rules.keys():
        input_text = re.sub(syntax_rules[key], group_coloring, input_text)

    coloured_text += input_text
    return coloured_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Colours strings in a file using rules from a syntax file and'
                                                 'a provided theme.')
    parser.add_argument('syntaxfile', type=str, help='Path to a syntax file')
    parser.add_argument('themefile', type=str, help='Path to a theme file')
    parser.add_argument('infile', type=str, help='Path to a file that will be coloured')
    args = parser.parse_args()
<<<<<<< HEAD
    #print(highlighter('./themes/java.syntax', './themes/java.theme', './examples/coloring_example.java'))
=======
    print(highlighter(args.syntaxfile, args.themefile, args.infile))
>>>>>>> f2f49b58d7aefcd7ec9df5ab9fb22293f21d11d6
