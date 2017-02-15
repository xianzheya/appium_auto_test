# -*- coding:utf-8 -*-

from unittest import TextTestRunner
from unittest import TestResult


class BaseRun(TextTestRunner):
    def __init__(self, stream):
        TextTestRunner.__init__(self)
        self.stream = stream

    def run(self, text):
        print(text)


class BaseResult(TestResult):
    def __init__(self):
        TestResult.__init__(self)
