# -*- coding:utf-8 -*-
import nose
import unittest
import test
class BaseTest(unittest.TestCase):
    def setUp(self):
        print("before test","s".capitalize())
    def tearDown(self):
        print("xz")

    class xz(unittest.TestLoader):
        def loadTestsFromModule(self, module, *args, pattern=None, **kws):
            print(dir(module))
            for name in dir(module):
                obj = getattr(module, name)
                print(module.__package__)
                # print(obj)
                break
            return "xz123"
    @unittest.skip
    def test_xz(self):
        assert 100 == 1001

    def test_s(self):
        assert 100 == 100
if __name__ == '__main__':
    # nose.runmodule()
    # nose.run()
    # unittest.main()
    print("********************")
    # print(unittest.TestLoader().loadTestsFromModule(test))
    print("21111")
    print(BaseTest().xz().loadTestsFromModule(test))
    print("********************")
    s = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    s1 = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    alltest = unittest.TestSuite([s,s1])
    print(alltest)
    # unittest.TextTestRunner(verbosity=2).run(alltest)