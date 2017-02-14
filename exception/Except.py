# -*- coding:utf-8 -*-

class ElementExcept(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "not found this element: {}".format(self.value)