# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from flask import Flask, make_response

app = Flask(__name__)


@app.route('/1.gif')
def hello_world():
    msg = """GIF89a
"""
    resp = make_response(msg)
    resp.mimetype = 'image/gif'
    resp.headers['Content-Transfer-Encoding'] = 'binary'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Accept-Ranges'] = 'bytes'

    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999)
