# -*- coding:utf-8 -*-

from schematics.models import  Model
from schematics.types import StringType

class ApkModel(Model):
    path = StringType()
    name = StringType()
    package = StringType()
    activity = StringType()