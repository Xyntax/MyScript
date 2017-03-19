# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests

ID = 'xKMcQwgccePal/jX7vU+Tg=='
TOKEN = 'CYPxwiyHXsfmoYYzTEvtNg=='
CIPHER = ID.decode('base64')
TRUE_IV = TOKEN.decode('base64')
LEN = len(TRUE_IV)


def xor_str(a, b):
    if len(a) != len(b):
        return False

    c = ''
    for i in range(0, len(a)):
        c += chr(ord(a[i]) ^ ord(b[i]))

    return c


def xor(a, b):
    return chr(ord(a) ^ ord(b))


def split_cipher_block(ciphertext, block_size=8):
    if len(ciphertext) % block_size != 0:
        return False

    result = []
    length = 0
    while length < len(ciphertext):
        result.append(ciphertext[length:length + block_size])
        length += block_size

    return result


def check_webpage(iv_base64):
    cookie = {
        'ID': ID,
        'token': iv_base64.strip(),
        'PHPSESSID': 'vmea2anf61u9s87gk3sr63hbd5'
    }
    r = requests.get('http://218.2.197.235:23737/index.php', cookies=cookie)
    # print r.content, r.status_code
    if 'ERROR' in r.content:
        return False
    else:
        print(r.content, r.status_code)
        return True


def collision():
    iv = list(TRUE_IV)
    intermediary = ''
    plain = ''
    for i in xrange(LEN):
        target_position = chr(i)
        print('getting target position: %s' % target_position.encode('hex'))
        for b in range(0, 256):
            iv[-1] = chr(b)
            iv_string = ''.join([ch for ch in iv])
            # print('testing: '+iv_string.encode('hex'))
            # print('checking: %d, %s' % (b, iv_string.encode('hex')))
            iv_base64 = iv_string.encode('base64')

            if check_webpage(iv_base64):
                # print(iv_string.encode('hex'))
                intermediary = xor(iv[-1], chr(i)) + intermediary
                plain += xor(intermediary, list(TRUE_IV)[-i]) + plain
                print('Plain Found: ' + plain.encode('hex'))


'0983f1c22c875ec7e6a186334c4bed33'
'0983f1c22c875ec7e6a186334c4bed36'  # origin


# print check_webpage(TOKEN)
# collision()


# print(xor(xor('\x33', '\x01'), '\x36').encode('hex'))  # 0x04
