# -*- coding:utf-8 -*-

import unittest
from server.appium_server import appiumDriver


class BaseTest(unittest.TestCase):
    pass
    # def setUpClass(cls):
    #     cls.driver = appiumDriver.appium_driver
    #
    # def tearDownClass(cls):
    #     cls.driver.close()
