#!/usr/bin/env python
# Youdao Dict

import sys
import urllib.parse
import urllib.request
import json

if sys.argv[1:] == []:
    print("Usage: {} word".format(sys.argv[0]))
    sys.exit(1)

url = 'http://fanyi.youdao.com/openapi.do'
data = {'keyfrom': 'YouDaoCV',
        'key': '659600698',
        'type': 'data',
        'doctype': 'json',
        'version': '1.1',
        'q': sys.argv[1]}

url_values = urllib.parse.urlencode(data)
full_url = url + '?' + url_values
with urllib.request.urlopen(full_url) as response:
    bytes = response.read()
    string = bytes.decode()
    js = json.loads(string)
    print(', '.join(js['translation']))
    print('\n'.join(js['basic']['explains']))
