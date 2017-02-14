# -*- coding:utf-8 -*-

import sys
import logging


def get_level(le=None):
    if le is None or le.lower() == "noset":
        return logging.DEBUG
    if isinstance(le, bytes):
        le = le.decode()
    if isinstance(le, str):
        try:
            le = int(le)
        except:
            if le.upper() in logging._nameToLevel.keys():
                return getattr(logging,le.upper())
            else:
                raise KeyError("please input ('CRITICAL:50','ERROR':40,'WARN','WARNING':30,'INFO':20,'DEBUG':10)")
    if isinstance(le, int):
        if le in logging._levelToName.keys():
            l = logging._levelToName[le]
        else:
            raise KeyError("please input ('CRITICAL:50','ERROR':40,'WARNING':30,'INFO':20,'DEBUG':10)")
    return getattr(logging,l)


class LoggerBase(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            org = super(LoggerBase, cls)
            cls._instance = org.__new__(cls)
        return cls._instance

    def __init__(self, logger_name="", file_name=None, level=None):
        if not self.__dict__:
            #print(self)
            self.loggername = logger_name
            self.fielname = file_name
            self.level = get_level(level)
            self.logger = logging.getLogger(self.loggername)
            self.logger.setLevel(self.level)
            formater = logging.Formatter(fmt="[ %(asctime)s ] %(name)s - %(levelname)s : %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
            if self.fielname is not None:
                fs = logging.FileHandler(self.filename)
                # fs.setLevel(self.level)
                fs.setFormatter(formater)
                self.logger.addHandler(fs)
            #cs = logging.StreamHandler(sys.stdout)
            ## cs.setLevel(self.level)
            #cs.setFormatter(formater)
            #self.logger.addHandler(cs)
        else:
            self.level = get_level(level)
            self.logger.setLevel(self.level)

    def info(self,mes=None):
        if mes is None:
            raise ValueError("mes not is None")
        if self.level == 50:
            self.logger.critical(mes)
        elif self.level == 40:
            self.logger.error(mes)
        elif self.level == 30:
            self.logger.warning(mes)
        elif self.level == 20:
            self.logger.info(mes)
        elif self.level == 10 or self.level == 0:
            self.logger.debug(mes)
