# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType

class PathFile(Model):
    aapt = StringType()
    adb = StringType()
    appium_server = StringType()
    apk_path = StringType()