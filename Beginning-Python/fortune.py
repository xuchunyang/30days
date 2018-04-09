#!/usr/bin/env python
#
# Page 145
#
# Usage: python fortune.py /usr/share/dict/words

"""
随机打印输入中的一行.
"""

import fileinput
import random

fortunes = list(fileinput.input())
print(random.choice(fortunes), end='')
