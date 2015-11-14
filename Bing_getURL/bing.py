# -*- coding: utf-8 -*-
import requests
import re
import sys
import time

"""
get URLs from Bing
xy 2015.11.13
"""


class getURLs(object):
    """docstring for getURLs"""

    def __init__(self):
        super(getURLs, self).__init__()

    def getURL(self, keyword, filename, page):
        page_count = 1

        print '[*] testing page 1'

        url = 'http://cn.bing.com/search?q=%s&first=' % keyword + str(page_count)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'utf-8;q=0.7,*;q=0.3'
        }

        r = requests.get(url)
        print '[*] Response: ' + str(r)

        page_content = r.content

        if page_content:
            print '[*] Get page content success!'
            # 以下代码方便调试正则使用
            file = open('first_page.html', 'w')
            file.write(page_content)
            file.close()
        else:
            print '[*] Cannot get content from URL!'
            sys.exit(0)
        oldpage_url = []
        oldpage_url = self.find_allURL(page_content)

        newpage_url = []
        all_url = []
        all_url.extend(oldpage_url)
        # 如果页面过大，超过实际，结果返回为首页，即新增url为0
        while oldpage_url != newpage_url:
            if page_count / 10 + 1 < int(page):
                # 这里+10表示下一页
                page_count += 10
                print '[*] downloading page %s' % (page_count / 10 + 1)
                url = 'http://cn.bing.com/search?q=%s&first=' % keyword + str(page_count)
                r = requests.get(url)
                page_content = r.content
                newpage_url = self.find_allURL(page_content)
                all_url.extend(newpage_url)
                all_url = [i for i in set(all_url)]
            else:
                print '[*] total pages: %s' % (page_count / 10 + 1)
                break

        print('[*] get URL: %s' % str(len(all_url)))
        print('[*] writing to file: %s ...' % filename)

        self.write_tofile(all_url, filename)

        print('[*] done!')

    # 正则
    def find_allURL(self, page_content):
        # reg_url = r'<h2><a href="(.*?)" target="_blank"'
        reg_url = r'<li class="b_algo"><h2><a href="(.*?)" target="_blank"'
        # reg_url = r'http://(.*?)&wd='
        onepage_url = []
        onepage_url = re.findall(reg_url, page_content)
        return onepage_url

    # 处理输出
    def write_tofile(self, all_url, filename):
        reg = r'<.{1,2}>'
        fobj = open(filename, 'a')
        fobj.writelines(['%s\n' % re.sub(reg, '', x) for x in all_url])
        fobj.close()


if __name__ == '__main__':
    print '[    Bing-URL-Tool     ]'
    print '[   edit by xy 151113  ]'
    print '[ any issues:i@cdxy.ME ]'
    geturls = getURLs()
    keyword = raw_input('keyword for searching: >')
    pages = raw_input('how many pages u want download? >')
    filename = str(time.clock()) + 'Bing_URLs'
    geturls.getURL(keyword, filename, pages)
