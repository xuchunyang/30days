#!/usr/bin/env python
# A simple cal(1) clone

"""
$ cal
     April 2018       
Su Mo Tu We Th Fr Sa  
 1  2  3  4  5  6  7  
 8  9 10 11 12 13 14  
15 16 17 18 19 20 21  
22 23 24 25 26 27 28  
29 30                 

"""

import time
import calendar

t = time.gmtime()
y, m, d = t.tm_year, t.tm_mon, t.tm_mday

print("     {} {}".format(calendar.month_name[m], y))
print("Su Mo Tu We Th Fr Sa")

m_days = calendar.monthrange(y, m)[1]

for i in range(1, m_days+1):
    if i == d:
        print("\033[7m" + str(i).rjust(2) + "\033[0m", end='')
    else:
        print("{0:2d}".format(i), end='')
    if i % 7 == 0:
        print()
    else:
        print(' ', end='')
print("\n")
