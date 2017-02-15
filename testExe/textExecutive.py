# -*- coding:utf-8 -*-

import test
import unittest
from baseCase.baseSuite import baseLoder


def test_executive():
    test_case = baseLoder.loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(test_case)

if __name__ == "__main__":
    test_executive()
