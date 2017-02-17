# -*- coding:utf-8 -*-

import sys
import os
import requests
import platform
import subprocess
from time import sleep
from appium import webdriver
from multiprocessing import Process
from api.WaitElement import utilTure as drwa
from server.Appium import Appium as appium
from server.apk_base import ApkBase as apk
from server.phone_base import PhoneBase as phone

__all__ = ['appiumDriver']


class AndroidSingle(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            org = super(AndroidSingle, cls)
            cls._instance = org.__new__(cls)
        return cls._instance


class AndroidServer(AndroidSingle):
    def __init__(self):
        if not self.__dict__:
            self.__apk = apk().apk
            self.__phone = phone().phone
            self.__appium = appium().appium
            self.n = 0

    def get_name(self):
        return self.__phone.device
    
    @property
    def appium_driver(self):
        desired_caps = {
            'device': 'Android',
            'platformName': 'Android',
            'deviceName': self.__phone.device,
            'browserName': '',
            'platformVersion': self.__phone.version,
            'app': self.__apk.path,
            'app-package': self.__apk.package,
            'app-activity': self.__apk.activity,
            'automationName': 'appium'
        }
        node = True
        if node:
            while node:
                self.__server_run
                sleep(3)
                if "windows" in platform.platform().lower():
                    p = subprocess.Popen("tasklist | findstr \"node\"", shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                    str_node = [li for li in p.stdout.readlines() if li.strip()]
                    if len(str_node):
                        node = False
                self.n += 1
                if self.n == 2:
                    print("please manual run '{}'".format(appium().appium.start))
                    sys.exit(1)
                continue
        driver = webdriver.Remote(self.__appium.url, desired_caps)
        try:
            self.__update_close(driver)
        except Exception:
            pass            
        return driver

    @property
    def __server_is_run(self):
        try:
            r = requests.get(self.__appium.status)
        except Exception:
            # print("appium server is not running ... ")
            return False
        code = r.status_code
        if code == 200:
            return True
        else:
            return False

    @property
    def __server_run(self):
        if not self.__server_is_run:
            print("appium server is starting ...")
            p = ServerRun()
            p.start()
    @property
    def server_stop(self):
        if self.__server_is_run:
            if os.name.lower() == 'nt':
                p = subprocess.Popen("tasklist | findstr \"node\"", shell=True,stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                name = p.stdout.read().split()[0].decode()
                subprocess.Popen(" ".join(["taskkill /IM", name]), shell=True)
            else:
                pass
        else:
            sys.exit(0)

    def server_restart(self):
        pass

    def __update_close(self,dr):
        if drwa(dr,"com.mqunar.atom.attemper:id/atom_atte_btn_download",25):
            dr.find_element_by_id("com.mqunar.atom.attemper:id/atom_atte_iv_close").click()


class ServerRun(Process):
    def __init__(self):
        super(ServerRun, self).__init__()
        self.r = appium().appium.start

    def run(self):
        subprocess.Popen(self.r, shell=True,close_fds=False)
appiumDriver = AndroidServer()

if __name__ == "__main__":
    a = AndroidServer()
    
    #print("xz")
    #print(a.get_name())
    ##sleep(20)
    #print("llllllll")
    #b = AndroidServer()
    #print(b.get_name())
    #a.server_stop


