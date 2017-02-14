# -*- coding:utf-8 -*-

from mode.Path import PathFile as pa
from config.path_f import get_path

class PathFile(object):
    def get(self):
        print(get_path())
        pa.config = get_path()
        return pa

if __name__ == "___main__":
    # p = PathFile()
    print(config.path_f)