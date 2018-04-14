import sys, re
from util import *

print("<html><head><title>...</title><body>")

title = True
for block in blocks(sys.stdin):
    block = re.sub(r"\*(.+?)\*", r"<em>\1</em>", block)
    if title:
        print(f"<h1>{block}</h1")
        title = False
    else:
        print(f"<p>{block}</p>")

print("</body></html>")
