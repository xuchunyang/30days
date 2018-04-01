#!/usr/bin/env python
# Clone of cat(1)

def cat(name):
    "Print the file contents."
    # TODO: 这里要做异常处理，失败的情况得跳过
    with open(name) as f:
        print(f.read(), end='')

if __name__ == "__main__":
    import sys
    names = sys.argv[1:]
    if names == []:
        print("Usage: {} [file ...]".format(sys.argv[0]))
    else:
        for x in names:
            cat(x)
