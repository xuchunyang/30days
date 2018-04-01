#!/usr/bin/env python
# Clone of cat(1)

def cat(name):
    "Print the file contents."
    try:
        f = open(name)
    except OSError as err:
        # https://misc.flogisoft.com/bash/tip_colors_and_formatting
        red = '\033[31m'
        reset = '\033[0m'
        print('{0}OSError: {1}: {2}{3}'.format(red, name, err, reset))
    else:
        print(f.read(), end='')
    finally:
        f.close()

if __name__ == "__main__":
    import sys
    names = sys.argv[1:]
    if names == []:
        print("Usage: {} [file ...]".format(sys.argv[0]))
    else:
        for x in names:
            cat(x)
