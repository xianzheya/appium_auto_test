# -*- coding:utf-8 -*-

def deco(func):
    print("before myfunc() called")
    func()
    print("after myfunc() called")
    return func

@deco
def myfunc():
    print("myfunc() called")


class a:
    @staticmethod
    def a():
        pass

# myfunc = deco(myfunc)
myfunc()