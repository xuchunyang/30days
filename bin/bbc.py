#!/usr/bin/env python
# Print Headline News from BBC

from requests_html import HTMLSession
session = HTMLSession()

r = session.get('http://www.bbc.com/news')

for a in r.html.find('a'):
    h = a.find('h3', first=True)
    if h:
        print(h.text)
        print(a.absolute_links.pop())
        break
