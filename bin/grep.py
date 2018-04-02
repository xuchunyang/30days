#!/usr/bin/env python
# Print matching lines
# 
# $ grep.py good /usr/share/dict/connectives

import sys
import re

# * Check command line arguments
if len(sys.argv) != 3:
    sys.stderr.write("Wrong number Of argument\n"
                     "Usage: {} PAT FILE\n")
    sys.exit(1)

pat, file = sys.argv[1:]
regexp = re.compile(pat)
with open(file) as f:
    linum = 1
    for line in f:
        if regexp.search(line):
            sys.stdout.write("{}:{}".format(linum, line))
        linum = linum + 1
