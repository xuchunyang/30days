#!/usr/bin/env python
# hr -- insert horizontal rule
#
# Clone of https://github.com/LuRsT/hr

import os
import sys

COLS = int(os.popen('tput cols', 'r').readline())

def hr(word):
    if word:
        print((word*COLS)[:COLS])

if sys.argv[1:]:
    for x in sys.argv[1:]:
        hr(x)
else:
    hr("#")
