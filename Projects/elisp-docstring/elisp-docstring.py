FUNCTION = 2
VARIABLE = 3

def split(line):
    sym, doc = line.split(sep="\n", maxsplit=1)
    if sym.startswith("F"):
        typ = FUNCTION
    else:
        typ = VARIABLE
    sym = sym[1:]
    return (sym, (typ, doc))

with open('DOC') as f:
    x = f.read()
    l = x.split(sep="\u001F")
    d = dict([split(i) for i in l if i])
