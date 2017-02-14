# -*-coding:utf-8 -*-

import pprint
#单例模式
class Singleton(object):
    # def __init__(self):
        # print self
        # print type(self)
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            print (cls)
            print (args)
            print (kw)
            org = super(Singleton, cls)
            # org = super.__init__(Singleton,cls)
            print (org)
            # pprint.pprint(dir(org))
            cls._instance = org.__new__(cls)
            # print cls
            # print type(cls)
        return cls._instance

class myClass(Singleton):
    a = 1

class m(myClass):
    pass
one = myClass(s="z")
two = myClass()
# print one
# print two
one = m()

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls,*args, **kwargs)
        # print ob
        ob.__dict__ = cls._state
        return ob

class myClass1(Borg):
    a = 1
one = myClass1()
two = myClass1()
one.a = 3
# print id(one.a)
# print id(two.a)
# print two.a

class Singleton2(type):
    def __init__(cls, name,bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance
class myClass3(object):
    __metaclass__ = Singleton2

one = myClass3()
two = myClass3()
# print one
# print two

def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
@singleton
class myClass4(object):
    a = 1
    def __init__(self, x = 0):
        self.x = x
one = myClass4()
two = myClass4()
# print one
# print two
# print id(one)
# print id(two)