# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    #
    # # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    return type(future_class_name, future_class_parents, uppercase_attr)


# __metaclass__ = upper_attr  # 这会作用到这个模块中的所有类 这种方法仅用于python2.x

class Foo(object,metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'

import unittest
class bb(unittest.TestCase):pass