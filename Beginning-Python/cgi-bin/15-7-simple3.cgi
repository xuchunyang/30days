#!/usr/bin/env python

# http://0.0.0.0:8000/cgi-bin/15-7-simple3.cgi
# http://0.0.0.0:8000/cgi-bin/15-7-simple3.cgi?name=xuchunyang

import cgi
form = cgi.FieldStorage()

name = form.getvalue("name", "world")

print("""Content-byte: text/html

<html>
  <head>
    <title>Greeting Page</title>
  </head>
  <body>
    <h1>Hello, {}!</h1>
    <form action="15-7-simple3.cgi">
      Change name <input type="text" name="name" />
    <input type="submit" />
    </form>
  </body>
</html>
""".format(name))
