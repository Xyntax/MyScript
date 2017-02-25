# !/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
A quick test for your payload

Usage: python quick.py <your_payload>
Example: python quick.py {{2+2}}
"""

import sys
from jinja2 import Template

if '-h' in sys.argv:
    print __doc__
else:
    print Template('[Output] {}'.format(sys.argv[1] if len(sys.argv) > 1 else '<empty>')).render()
