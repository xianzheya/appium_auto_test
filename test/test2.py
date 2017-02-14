# -*- coding:utf-8 -*-

import unittest
from baseCase.case import BaseTest
# class A(object):
#     def __init__(self):
#         self.__dict__ = {"c":1}
#
# a = A()
# print(a.c)
# print(A.__dict__)

#把这种字符串 'camelsHaveThreeHumps'  转化成这种camels-have-three-humps  如果里面有数字就删除
print("".join((map(lambda x: "-"+x.lower() if x.isupper() else x,[i for i in "camelsHaveThreeHu3333mps" if not  str.isdigit(i)]))))
def reverse_str( s ):
    return s[::-1]

# print(reverse_str("xzxzxz"))
# print("zx"[::-1])
# print([i for i in "xz"  if i.islower() ])


class ss(BaseTest):
    def runTest(self):pass