#!/usr/bin/env python
# Recursively find file by name

import sys
import os
import fnmatch

if len(sys.argv) != 2:
    print("Usage: {} glob".format(sys.argv[0]))
    sys.exit(1)

pattern = sys.argv[1]

for root, dirs, files in os.walk('.'):
    for f in fnmatch.filter(files, pattern):
        print(f)
