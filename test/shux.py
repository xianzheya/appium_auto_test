# -*- coding:utf-8 -*-
import urllib, re, urllib2


class QSBK:
    def __init__(self):  # 构造函数，self对象自身的引用
        self.pageindex = 1
        #         self.user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.story = []  # save story
        self.enable = False  # if can continue save

    def getpage(self, pageindex):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/' + str(pageindex)
            #             print url
            request = urllib2.Request(url, headers=self.header)
            print request.get_full_url()
            openurl = urllib2.urlopen(request).read()
            print openurl
            # return openurl
            print openurl
        except urllib2.URLError, e:
            print
            u'打开网址失败：', e
            #         except AttributeError,e:
            #             print e

    def start(self):
        self.getpage(1)


l = QSBK()
l.start()
