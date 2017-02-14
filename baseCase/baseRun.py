# -*- coding:utf-8 -*-

from unittest import TextTestRunner
from unittest import  TestResult


class BaseRun(TextTestRunner):
    def __init__(self):
        TextTestRunner.__init__(self)

    def run(self, text):
        print(text)


class BaseResult(TestResult):
    def __init__(self):
        TestResult.__init__(self)




baseRun = BaseRun()