# -*- coding:utf-8 -*-

from unittest.result import TestResult
from unittest import TextTestRunner
from server.log import LoggerBase


class BaseResult(TestResult):
    def __init__(self, stream, descriptions, verbosity):
        super(BaseResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions
        self.log = LoggerBase("appium", level="info")

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return str(test)

    def startTest(self, test):
        super(BaseResult, self).startTest(test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")
            self.stream.flush()
            self.log.info("测试开始")
            self.log.info("测试开始执行第 {} 条......".format(self.testsRun))

    def addSuccess(self, test):
        super(BaseResult, self).addSuccess(test)
        if self.showAll:
            self.stream.writeln("ok")
            self.log.info("测试执行第 {} 条执行成功".format(self.testsRun))
        elif self.dots:
            self.stream.write('.')
            self.stream.flush()

    def addError(self, test, err):
        super(BaseResult, self).addError(test, err)
        if self.showAll:
            self.stream.writeln("ERROR")
            self.log.info("测试执行第 {} 条执行失败".format(self.testsRun))
        elif self.dots:
            self.stream.write('E')
            self.stream.flush()

    def addFailure(self, test, err):
        super(BaseResult, self).addFailure(test, err)
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.write('F')
            self.stream.flush()

    def addSkip(self, test, reason):
        super(BaseResult, self).addSkip(test, reason)
        if self.showAll:
            self.stream.writeln("skipped {0!r}".format(reason))
        elif self.dots:
            self.stream.write("s")
            self.stream.flush()

    def addExpectedFailure(self, test, err):
        super(BaseResult, self).addExpectedFailure(test, err)
        if self.showAll:
            self.stream.writeln("expected failure")
        elif self.dots:
            self.stream.write("x")
            self.stream.flush()

    def addUnexpectedSuccess(self, test):
        super(BaseResult, self).addUnexpectedSuccess(test)
        if self.showAll:
            self.stream.writeln("unexpected success")
        elif self.dots:
            self.stream.write("u")
            self.stream.flush()

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s" % (flavour,self.getDescription(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln("%s" % err)



class BaseRunner(TextTestRunner):
    resultclass = BaseResult