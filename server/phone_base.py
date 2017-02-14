# -*- coding: utf-8 -*-

import re
from subprocess import Popen
from subprocess import PIPE
from mode.ConfigModel import ConfigModel
from mode.PhoneModle import PhoneModle as phone1

class PhoneBase(object):
    '''
        这是获取手机的基本信息
    '''
    def __init__(self):
        self.con = ConfigModel
        
        
    # 获取手机的版本
    def __version(self):
        pile = re.compile(br"=[0-9]\.[0-9](\.[0-9])?")
        device = self.__devices
        try:
            if not device:
                raise AttributeError
            cmd = "".join(["adb -s ", device, " shell cat /system/build.prop"])
            result = Popen(cmd, shell=True, stdout=PIPE)
            s = result.stdout.read()
            #e = result.stderr.read()
            result_s = pile.search(s)
            version = result_s.group(0)[1:]
            ver = version.decode("utf-8")
        except AttributeError as e:
            try:
                ver = self.con.version
            except:
                raise AttributeError("please at 'config.ini' file write version=?")
        return ver
    #获取连接手机的devices名 取第一个
    @property
    def __devices(self):
        cmd = "adb devices -l "
        try:
            result = Popen(cmd, shell=True, stdout=PIPE)
            result_s = [i.strip() for i in  result.stdout.readlines() if i.strip() if not i.lower().startswith(b"emulator")]
            if len(result_s) <= 1:
                raise ValueError
            device = result_s[-1].split()[0]
            driv = device.decode("utf-8")
        except ValueError as e:
            driv = ''
        return driv

    def __devicename(self):
        cmd = "adb devices -l "
        try:
            result = Popen(cmd, shell=True, stdout=PIPE)
            result_s = [i.strip() for i in  result.stdout.readlines() if i.strip() if not i.lower().startswith(b"emulator")]
            device = re.search(rb"model:(.*? )",result_s[-1])
            name = device.group(1).decode("utf-8")
        except AttributeError as e:
            try:
                name = self.con.drivername
            except:
                raise AttributeError("please at 'config.ini' file write drivername=?")
        return name

    @property
    def phone(self):
        d = {}
        d["version"] = self.__version()
        d["device"] = self.__devicename()
        p = phone1(d)
        return p
if __name__ == '__main__':
    c = PhoneBase()
    d = c.phone
    print(d.device, d.version)