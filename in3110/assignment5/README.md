# Assignment 5

## 5.1

**highlighter.py** highlights source code files according provided syntax rules and theme.

Note: The highlighter should not highlight sub-strings within comments and strings.

Usage: `./highlighter.py syntax theme source`

For demo run `./demo_py_java.py`

## 5.2

**Python syntax**:
- Block comments
- Inline comments
- Function definition
- Function name
- Class definition
- Class name
- String
- Import statement
- True, False, None
- For
- While
- If, elif, else
- try, except
- in, and, or, is, not
- Decorator

## 5.3

**Java syntax**:
- Block comments
- Inline comments
- String
- Class definition
- Class name
- Keywords: abstract, extends, public, private
- Arithmetic operators
- Return

## 5.4

**grep.py** prints out strings that contain matching regular expressions and can highlight it.

Usage: `./grep.py source regex1 [regex2 ...] --highlight`

For demo run `./demo_grep.py`

## 5.5 & 5.6

**diff.py** finds the difference between two files and highlights the strings that differ.

Usage: `./diff.py text1 text2`

For demo run `./demo_diff.py`

## Demo

In order to run all demos, run `./demo.py`

`/examples` folder contains the files required for the demos. `/themes` folder contains theme and syntax files.