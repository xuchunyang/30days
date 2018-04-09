#!/usr/bin/env python
#
# $ python hello-doctest.py -v

def square(x):
    """
    返回平方根.
    >>> square(2)
    4
    >>> square(5)
    25
    """
    return x * x

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
