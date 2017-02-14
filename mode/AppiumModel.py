# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType


class AppiumModel(Model):
    url = StringType()
    start = StringType()
    status = StringType()