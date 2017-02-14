# -*- coding:utf-8 -*-

import os
import re
from mode.ApkModel import ApkModel
import subprocess
from mode.ConfigModel import ConfigModel as conf

class ApkBase(object):
    def __init__(self):
        self.p = conf

    def __get_activity(self, mod):
        d = {}
        apk = self.__path_apk()
        d["name"] = os.path.normpath(apk).split("\\")[-1]
        d["path"] = apk
        if mod == 1 and conf.package and conf.activity:
            d["package"] = conf.package
            d["activity"] = conf.activity
        else:
            mod = 2
        if mod == 2:
            cmd = "aapt dump badging " + apk
            p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
            app_b = p.stdout.read()
            package = re.search(rb"package: name='(.*?)'",app_b)
            d["package"] = package.group(1).decode("utf-8")
            activity = re.search(rb"launchable-activity: name='(.*?)'",app_b)
            d["activity"] = activity.group(1).decode("utf-8")

        p = ApkModel(d)
        return p

    def __path_apk(self):
        if self.p.apk_path != '':
            if os.path.splitext(self.p.apk_path)[1] != ".apk":
                raise ValueError("please write correct apk path")
            elif not os.path.exists(self.p.apk_path) :
                raise FileExistsError(self.p.apk_path + " is not exists")
            return self.p.apk_path
        else :
            pa = os.path.normpath(os.path.abspath(os.pardir)+"/app")
            app_list= os.listdir(pa)
            for i in app_list:
                if os.path.splitext(i)[1] == ".apk":
                    paf = os.path.join(pa,i)
                    return paf
                else:
                    raise FileExistsError("This app folder not exists apk")
    @property
    def apk(self):
        if hasattr(conf, "package") and hasattr(conf, "activity"):
            a = self.__get_activity(1)
        else:
            a = self.__get_activity(2)
        return a
if __name__ == '__main__':
    ap = ApkBase()
    a = ap.apk
    print(a.activity)

