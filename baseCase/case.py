#-*- coding:utf-8 -*-

import unittest
from server.appium_server import AndroidServer

class BaseTest(unittest.TestCase):
    def setUp(self):
        pass
        # self.driver = AndroidServer().appium_driver
    def tearDown(self):
        pass
        # self.driver.close()