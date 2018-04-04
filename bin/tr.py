#!/usr/bin/env python
# echo $PATH | tr.py : '\n'

import sys

old, new = sys.argv[1:]

# print(repr(old))
# print(repr(new))

old = old.replace('\\n', '\n')
new = new.replace('\\n', '\n')

# print(repr(old))
# print(repr(new))

table = str.maketrans(old, new)
string = sys.stdin.read()
print(string.translate(table), end='')
