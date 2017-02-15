# -*- coding:utf-8 -*-

import test
import unittest
import sys
from baseCase.baseSuite import baseLoder
from baseCase.baseLog import BaseRunner


def test_executive():
    test_case = baseLoder.loadTestsFromModule(test)
    try:
        f = open("txt.txt", "w")
        # unittest.TextTestRunner(f, verbosity=2).run(test_case)
        BaseRunner(f, verbosity=2).run(test_case)
    finally:
        f.close()

if __name__ == "__main__":
    test_executive()
