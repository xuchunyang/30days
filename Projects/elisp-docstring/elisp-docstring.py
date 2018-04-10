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

from flask import Flask, url_for, request, abort, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Emacs Lisp Docstring"

@app.route('/<name>')
def lookup(name):
    if name in d:
        sym = name
        typ, doc = d[name]
        app.logger.debug(repr(doc))
        return render_template('show_entry.html', sym=name, typ=typ, doc=doc)
    else:
        abort(404)
