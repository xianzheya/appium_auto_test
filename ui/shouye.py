# -*- coding:utf-8 -*-

from server.appium_server import AndroidServer as server


class ShouYe(object):
    def __init__(self):
        self.driver = server().appium_driver

    def tishi(self):
        try:
            return self.driver.find_elements_by_android_uiautomator("android:id/button2")
        except Exception:
            return False
