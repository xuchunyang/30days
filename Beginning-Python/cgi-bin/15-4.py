#!/usr/bin/env python
# * Open HTTP server
# $ python -m http.server --cg
# * Check the result
# http://0.0.0.0:8000/cgi-bin/15-4.py

print("Content-type: text/html\n")
print("hello, world!")
