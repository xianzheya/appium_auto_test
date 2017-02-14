# -*- coding:utf-8 -*-

class AutoConfig(type):
    def __new__(cls,name,bases,dic):
        d = dic['_'+name+'__d']
        return super(AutoConfig,cls).__new__(cls,name,bases,d)