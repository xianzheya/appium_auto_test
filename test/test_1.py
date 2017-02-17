# -*- coding:utf-8 -*-

from baseCase.case import BaseTest
from server.log import LoggerBase


class test(BaseTest):
    def test1(self):
        """ 测试首页的小入口个数 """
        self.assertEquals(1,2)

    def test2(self):
        """ceshi nihao"""
        self.assertEquals(2,1)

    def xz(self):
        self.assertEquals(1,1)
class tew(BaseTest):
    def test(self):
        self.assertEquals(1,1,"kkk")