# -*- coding:utf-8 -*-

import re
from config.path_f import get_path

def __chuli(i):
    i_g = i.replace("\"", "").replace("\'","")
    i_list = i_g.split("=")
    for i in range(len(i_list)):
        i_list[i] = i_list[i].strip()
    if ' ' in i_list[1]:
        i = "=".join([i_list[0],"".join(['"',i_list[1],'"'])])
    else:
        i = "=".join([i_list[0],  i_list[1]])
    return list(map(str,i.split("=")))

def get_config():
    path_f = get_path()
    with open(path_f, mode="r", encoding="utf-8") as f:
        con = f.read()
    l = re.findall(r".*=.*",con)
    con_dicct = dict(list(map(__chuli,l)))
    return con_dicct

def get_dict():
    path_f = get_path("dict.ini")
    with open(path_f, mode="r", encoding="utf-8") as f:
        con = f.read()
    l = re.findall(r".*=.*", con)
    con_dicct = dict(list(map(__chuli, l)))
    # c = ConfigModel(con_dicct)
    # return c

if __name__ == "__main__":
    a = get_config()
    print(a)
