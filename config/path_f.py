# -*- coding:utf-8-*-

import os

def get_path(pr="config.ini"):
    return os.path.join(os.path.dirname(__file__), pr)