#!/usr/bin/env python
# Print Hacker News Titles & URLs

from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://news.ycombinator.com/')

i = 1
for elt in r.html.find('.storylink'):
    print('{0:2d}. {1}'.format(i, elt.text))
    print('    ' + elt.absolute_links.pop())
    print()
    i = i + 1
