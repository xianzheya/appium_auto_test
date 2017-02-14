# -*- coding:utf-8 -*-

from config.get_config import get_config
from mode.BaseMode import AutoConfig

class ConfigModel(object,metaclass=AutoConfig):
    __d=get_config()

if __name__ == "__main__":
    q = ConfigModel
    print(q.driver)
    print(ConfigModel.__dict__)

