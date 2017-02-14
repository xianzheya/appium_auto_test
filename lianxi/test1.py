# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
# class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    # def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
    #     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    #     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    #     return type(future_class_name, future_class_parents, uppercase_attr)


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
# class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
#     def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
#         attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#         uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#         return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# class UpperAttrMetaclass(type):
#     def __new__(cls, name, bases, dct):
#         attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
#         uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
#         return type.__new__(cls, name, bases, uppercase_attr)

# class UpperAttrMetaclass(type):
#     def __new__(cls, name, bases, dct):
#         print(dct)
#         attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
#         uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#         return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
#
#
# class Foo(object,metaclass=UpperAttrMetaclass):
#     bir="b"
#     def d(self):
#         pass
#     b = {"a":1}
from baseCase.case import BaseTest
import unittest
import test,os,sys,pprint
class aa(BaseTest):
    def a(self):pass
    def test_x(self):
        self.assertEqual(1,1)
    def teSt_d(self):
        self.assertEqual(2,3)
    def runTest(self):
        pass
    # def __call__(self):
    #     return 2
# print(Foo)
# print(hasattr(Foo,"BIR"))

if __name__ == "__main__":
    print(callable(getattr(aa,"test_d")))
    # print("o")
    # dir_name = os.listdir(os.path.dirname(test.__file__))
    # print(dir_name)
    # tests1 = [n[:-3] for n in dir_name if n.startswith("test") or n.startswith("Test") or n.startswith("TEST")]
    # print(tests1)
    # clna = "".join([test.__package__,".",tests1[0]])
    # print(clna)
    # s = __import__(clna,fromlist=True)
    # print(dir(s))
    # print("**********")
    # for i in dir(s):
    #     obj = getattr(s,i)
    #     if isinstance(obj,type) and issubclass(obj,BaseTest):
    #         print(callable(obj))
    # print(s)
    # print(callable(s.__name__))
    # print("********g******")
    # pprint.pprint(sys.modules)
    # g = globals()
    # pprint.pprint(BaseTest.__subclasses__())
    # s = unittest.TestLoader().loadTestsFromTestCase(aa)
    # unittest.TestSuite().run(s)