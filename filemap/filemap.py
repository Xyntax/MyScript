# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import os
import sys
from itertools import chain
import glob

try:
    web_path = sys.argv[1]
    ext = sys.argv[2]
except IndexError:
    sys.exit("Example: python filemap.py /var/www/wordpress *.php")

result = (chain.from_iterable(glob.iglob(os.path.join(x[0], ext)) for x in os.walk(web_path)))

html = '<html lang="en"><head><meta charset="UTF-8"><title>filemap</title></head><body><ul>'
for path in result:
    path = path.replace(web_path, './')
    html += '<li><a href="{}">{}</a></li>'.format(path, path)
html += '</ul></body></html>'

with open(os.path.join(web_path, 'filemap.html'), 'w') as f:
    f.write(html)
