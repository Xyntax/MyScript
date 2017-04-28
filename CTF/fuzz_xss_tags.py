# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
from string import punctuation,whitespace

URL = 'https://router.vip/preview.php'

on = ['onafterprint', 'onbeforeprint', 'onbeforeunload', 'onerror', 'onhaschange', 'onload', 'onmessage',
      'onoffline', 'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onredo', 'onresize', 'onstorage',
      'onundo', 'onunload', 'onblur', 'onchange', 'oncontextmenu', 'onfocus', 'onformchange', 'onforminput', 'oninput',
      'oninvalid', 'onreset', 'onselect', 'onsubmit', 'onkeydown', 'onkeypress', 'onkeyup', 'onclick',
      'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart',
      'ondrop', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel',
      'onscroll', 'onabort', 'oncanplay', 'oncanplaythrough', 'ondurationchange', 'onemptied',
      'onended', 'onerror', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onpause', 'onplay', 'onplaying',
      'onprogress', 'onratechange', 'onreadystatechange', 'onseeked', 'onseeking', 'onstalled', 'onsuspend',
      'ontimeupdate', 'onvolumechange', 'onwaiting']

tag = ['<!-->', '<!DOCTYPE>', '<a>', '<abbr>', '<acronym>', '<address>', '<applet>', '<area>', '<article>',
       '<aside>', '<audio>', '<b>', '<base>', '<basefont>', '<bdi>', '<bdo>', '<big>', '<blockquote>', '<body>', '<br>',
       '<button>', '<canvas>', '<caption>', '<center>', '<cite>', '<code>', '<col>', '<colgroup>', '<command>',
       '<datalist>', '<dd>', '<del>', '<details>', '<dfn>', '<dialog>', '<dir>', '<div>', '<dl>', '<dt>', '<em>',
       '<embed>', '<fieldset>', '<figcaption>', '<figure>', '<font>', '<footer>', '<form>', '<frame>', '<frameset>',
       '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<head>', '<header>', '<hr>', '<html>', '<i>', '<iframe>',
       '<img>', '<input>', '<ins>', '<kbd>',
       '<keygen>', '<label>', '<legend>', '<li>', '<link>', '<main>', '<map>', '<mark>', '<menu>', '<menuitem>',
       '<meta>', '<meter>', '<nav>', '<noframes>', '<noscript>', '<object>', '<ol>', '<optgroup>', '<option>',
       '<output>', '<p>', '<param>', '<pre>', '<progress>', '<q>', '<rp>', '<rt>', '<ruby>', '<s>', '<samp>',
       '<script>', '<section>', '<select>', '<small>', '<source>', '<span>', '<strike>', '<strong>', '<style>', '<sub>',
       '<summary>', '<sup>', '<table>', '<tbody>', '<td>', '<textarea>', '<tfoot>', '<th>', '<thead>', '<time>',
       '<title>', '<tr>', '<track>', '<tt>', '<u>', '<ul>', '<var>', '<video>', '<wbr>']


# def get_tags():
#     ans = []
#     for each in tag.split('\n'):
#         ans.append(each.strip())
#     print ans

filtered = []
passed = []


def check_one(str):
    DATA = {'task': '',
            'payload': '%s' % str}
    r = requests.post(URL, data=DATA)
    # print(r.status_code, r.content)
    if r.status_code == 200 and 'XSS Test Page' in r.content:
        passed.append(str)
        # print str
    else:
        filtered.append(str)


def fuzz():
    # for each in on:
    #     check_one(each)
    # for each in tag:
    #     check_one(each)
    for each in punctuation+whitespace:
        check_one(each)

    print(passed)
    print(filtered)


fuzz()
# check_one('onload')
