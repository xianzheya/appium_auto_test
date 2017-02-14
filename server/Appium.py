# -*- coding:utf-8 -*-

from mode.AppiumModel import AppiumModel as ap
from mode.ConfigModel import ConfigModel as conf
from server.join import join
import os,sys


class Appium(object):

    def __init__(self):
        g = conf
        self.__config = g.server_path
        self.par = g.appium_par
        self.__ip = g.ip
        self.__port = g.port
        self.__d = {}

    def __run_command(self):
        file1 = os.path.splitext(self.__config)
        if file1[1] == '':
            if self.par is None:
                cmd = join(self.__config, "appium.js")
            else:
                cmd = join(self.__config, "appium.js",self.par)
        else:
            if self.par is None:
                cmd = self.__config
            else:
                cmd = join(self.__config,self.par)
        if os.name in ["NT","nt"]:
            command = "".join(["start node ", cmd])
        else:
            command = "".join(["node ", cmd])
        self.__d['start'] = command

    def __url(self):
        url = "http://{url}:{port}/wd/hub".format(url=self.__ip,port=self.__port)
        status = "http://{url}:{port}/wd/hub/status".format(url=self.__ip,port=self.__port)
        self.__d['url'] = url
        self.__d['status'] = status

    @property
    def appium(self):
        self.__run_command()
        self.__url()
        a = ap(self.__d)
        return a

if __name__ == '__main__':
    a = Appium()
    print(a.appium.status)
    print(sys.version)
