# !/usr/bin/env python
# -*- encoding: utf-8 -*-

import Queue
import sys
import threading
import time
import optparse
import requests
from lib.consle_width import getTerminalSize


class sshBrute:
    def __init__(self, threads_num, pass_dic, user_dic, target_dic):

        # 目标列表 用户名 和密码字典
        self.pass_dic = pass_dic
        self.user_dic = user_dic
        self.target_dic = target_dic

        self.pass_list = []
        self.user_list = []
        self.target_list = []

        self.thread_count = self.threads_num = threads_num
        self.scan_count = self.found_count = 0

        self.lock = threading.Lock()

        self.console_width = getTerminalSize()[0]
        self.console_width -= 2  # Cal width when starts up

        self.outfile = './output.txt'
        # self.outfile = open(outfile, 'w')  # won't close manually
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self._generate_queue()
        self._read_dicts()

    # 生成队列
    def _generate_queue(self):
        self.queue = Queue.Queue()
        for _target in self.target_list:
            for _user in self.user_list:
                for _pass in self.pass_list:
                    self.queue.put([_target, _user, _pass])

    # 读取文件内容到list
    def _read_dicts(self):
        for each in open(self.user_dic):
            self.user_list.append(each.strip())
        for each in open(self.pass_dic):
            self.pass_list.append(each.strip())
        for each in open(self.target_dic):
            self.target_list.append(each.strip())

    def _update_scan_count(self):
        self.lock.acquire()
        self.scan_count += 1
        self.lock.release()

    def _print_progress(self):
        self.lock.acquire()
        msg = '%s found | %s remaining | %s scanned in %.2f seconds' % (
            self.found_count, self.queue.qsize(), self.scan_count, time.time() - self.start_time)
        sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        sys.stdout.flush()
        self.lock.release()

    def _scan(self):
        while self.queue.qsize() > 0:
            payload = self.queue.get(timeout=1.0)
            try:
                self.test(payload[0], payload[1], payload[2])
            except:
                pass
            self._update_scan_count()
            self._print_progress()
        self._print_progress()
        self.lock.acquire()
        self.thread_count -= 1
        self.lock.release()

    def run(self):
        self.start_time = time.time()
        for i in range(self.threads_num):
            t = threading.Thread(target=self._scan, name=str(i))
            t.setDaemon(True)
            t.start()
        while self.thread_count > 0:
            time.sleep(0.01)

    def test(self, _target, _user, _pass):
        if True:
            self.write_log(_target + ' ' + _user + ' ' + _pass + ' \n')

    def write_log(self, string):
        self.lock.acquire()
        f = open(self.outfile, 'a')
        f.write(string)
        f.close()
        self.found_count += 1
        self.lock.release()


if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options] target')
    parser.add_option('-t', '--threads', dest='threads_num',
                      default=10, type='int',
                      help='Number of threads. default = 30')
    parser.add_option('-T', '--target', dest='target_dic', default=None,
                      type='string', help='target_dic')
    parser.add_option('-U', '--user', dest='user_dic', default=None,
                      type='string', help='user_dic')
    parser.add_option('-P', '--pass', dest='pass_dic', default=None,
                      type='string', help='pass_dic')
    (options, args) = parser.parse_args()
    # if len(args) < 1:
    #     parser.print_help()
    #     sys.exit(0)

    d = sshBrute(target_dic=options.target_dic,
                 user_dic=options.user_dic,
                 pass_dic=options.pass_dic,
                 threads_num=options.threads_num,
                 )
    d.run()
