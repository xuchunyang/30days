#!/usr/bin/env python
# Print 'y', forever

import sys

s = 'y'
if sys.argv[1:]:
    s = sys.argv[1]

while True:
    print(s)
