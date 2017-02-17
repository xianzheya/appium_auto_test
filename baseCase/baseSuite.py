# -*-coding:utf-8 -*-

import os
import test
import functools
from unittest.loader import TestLoader
from baseCase.case import BaseTest


class BaseLoader(TestLoader):
    def loadTestsFromTestCase(self, testCaseClass):
        def isTestMethod(arr, testClass=testCaseClass):
            return arr[:4].lower().startswith('test') and callable(
                getattr(testClass, arr)) or arr == "runTest" and callable(getattr(testClass, arr))
        testFnNames = list(filter(isTestMethod, dir(testCaseClass)))
        if self.sortTestMethodsUsing:
            testFnNames.sort(key=functools.cmp_to_key(self.sortTestMethodsUsing))
        loaded_suite = self.suiteClass(map(testCaseClass, testFnNames))
        return loaded_suite

    def loadTestsFromModule(self, module, *args, pattern=None, **kws):
        dir_name = os.listdir(os.path.dirname(module.__file__))
        tests1 = [n[:-3] for n in dir_name if n.lower().startswith("test")]
        [__import__("".join([str(module.__package__), '.', i]), fromlist=True) for i in tests1]
        itests = self.suiteClass(map(self.loadTestsFromTestCase, BaseTest.__subclasses__()))
        return itests

baseLoder = BaseLoader()

if __name__ == "__main__":
    b = BaseLoader()
    s = b.loadTestsFromModule(test)
    print(s)
    # unittest.TextTestRunner(verbosity=2).run(s)