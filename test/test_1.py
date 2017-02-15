# -*- coding:utf-8 -*-

from baseCase.case import BaseTest
from server.log import LoggerBase

class test(BaseTest):
    def  test1(self):
        self.assertEquals(1, 1)
        LoggerBase().info("xz")