#!/usr/bin/env python
# seq [-w] [beg] end

import sys

def help():
    print("Usage: {} [-w] [beg] end")
    sys.exit(1)

def seq(args):
    fixed_width = False
    beg = 1
    end = None
    if args.count('-w') == 1:
        fixed_width = True
        args.pop(args.index('-w'))
    if len(args) == 1:
        end = int(args[0])
    elif len(args) == 2:
        beg, end = [int(x) for x in args]
    else:
        help()
    for i in range(beg, end+1):
        if fixed_width:
            max_width = len(str(end))
            print(("{0:0" + str(max_width) + "d}").format(i))
        else:
            print(i)

def main():
    seq(sys.argv[1:])

if __name__ == '__main__':
    main()
