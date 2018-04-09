#!/usr/bin/env python
# cat along side with line number
#
# bash$ diff <(nl nl.py) <(./nl.py nl.py )

import fileinput

lineno = 0
for line in fileinput.input():
    line = line.rstrip()
    if line:
        lineno += 1
    else:
        print("{:>6} ".format(" "))
        continue
    print("{0:>6}\t{1}".format(lineno, line))
