 # -*- coding:utf-8 -*-
#
# from openpyxl import Workbook
# import openpyxl
#
# file1 = r"d:\trafficTabSort.dic"
# file2 = r"d:\提供智能中转的A-B_can.xlsx"
#
# with open(file1,"rb") as f:
#     l = [i.decode().strip() for i in f if i.strip()]
#
# print(l)
#
# p = openpyxl.load_workbook(file2)
#
# w = p.active
# lll = []
# for j, k in enumerate(w.rows):
#     for nn in k:
#         lll.append(nn.value)
#     # print(lll)
#     for n in l:
#         ll = n.split("\t")
#         # print(ll)
#         if ll[0] == lll[0] and ll[1] == lll[1]:
#             w.cell(row=j+1,column=4,value=ll[2])
#             w.cell(row=j+1,column=5,value=' '.join(ll[:-1]))
#             print(lll)
#             print(ll)
#     del lll[:]
# p.save(file2)

import sys
sys.path.insert(0,"D:\Program Files\Sublime Text 3")
# import sublime_plugin
# print(dir(sublime_plugin))
print(getattr())