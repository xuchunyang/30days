#!/usr/bin/env python
# A simple clone of wc(1)

import sys

def wc(filename):
    "Print the number of lines, words and bytes."
    line, word, byte = 0, 0, 0
    if filename == '-':
        f = sys.stdin
    else:
        try:
            f = open(filename)
        except:
            sys.stderr.write("Can't read {}\n".format(filename))
    for s in f:
        if s[-1] == '\n':
            line = line + 1
        byte = byte + len(s)
        word = word + len(s.split())
    print("{} has {} lines, {} words, and {} characters".format(filename, line, word, byte))
    f.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        filenames = ['-']
    else:
        filenames = sys.argv[1:]
    for f in filenames:
        wc(f)
