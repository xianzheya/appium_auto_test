# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType

class PhoneModle(Model):
    version = StringType() # 手机的类型
    device = StringType() # 设备名
