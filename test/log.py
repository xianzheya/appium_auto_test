# -*- coding:utf-8 -*-

import logging
import pprint
import sys

# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',filename='d:\myapp.log',filemode='w',stream="")

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%A %d %b %Y %H:%M:%S',stream=sys.stdout)
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# logging.getLogger("").addHandler(console)
# logging.debug("this is debug")
logging.info("this is info ")
# logging.getLogger().info("this is info ")

#创建logger
# logger = logging.getLogger("myLogger")
# logger.setLevel(logging.INFO)

# #创建一个handler，用于写入日志文件
# fh = logging.FileHandler("test.txt")
# fh.setLevel(logging.DEBUG)

# #再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# #定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s-%(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# #给log添加handler
# logger.addHandler(fh)
# logger.addHandler(ch)

# #记录一条日志
# # logger.info("this is INFO")
# # logger.info("xz123")
# pprint(dir(logger.i))