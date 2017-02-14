# -*- coding:utf-8 -*-
# # import xlwt, xlrd
# import urllib, re
# from openpyxl import Workbook
#
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')#调试时候处理中文，并且输出的是utf-8格式
# '''
# 取网页源码，filter正则，写入文件
# 注意字符编码，page是可以自定义的
# 注意网页chara是gbk,格式所以打印需要转码，如果转码之后输入文件会报错，因为是gbk格式，所以还要将gbk格式再次编码encode utf-8
# '''
#
#
# def get_content(page=None):
#     url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=python&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(
#         page)
#     print url
#     html = urllib.urlopen(url).read().decode('gbk')
#     return html
#
#
# def get(html):
#     reg = re.compile(
#         r'class="t1 ".*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>',
#         re.S)
#     # re.S匹配换行符
#     items = re.findall(reg, html)
#     #     print items
#     #     for i in items:
#     #         print i[0]+'\t',i[1]+'\t',i[2]+'\t',i[3]
#     return items
#
#
# # a=get_content(1)
# # get(a)
# # i = 0
# # for j in range(1, 2):
# #     html = get_content(j).encode('utf-8')  # encode utf-8格式
# #     for i in get(html):
# #         content = i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3] + '\n'
# #         print
# #         content
# def main():
#     h = get_content(4)
#     l =  get(h)
#     workboot = Workbook()
#     # p =
#     sheet = workboot.create_sheet(u"职位",0)
#     sheet1 = workboot.create_sheet(u"职位1", 1)
#     for j in l:
#         # print j
#         sheet.append(j)
#     # workboot.save(u"d:\\职位.xlsx")
#     print type(sheet.rows)
#     for e in sheet.rows:
#         for ee in e:
#             print ee.value
#     # for i, j in enumerate(l):
#     #     print " ".join(j)
#     #     sheet1.cell(row=i+1,column=1,value=" ".join(j))
#     workboot.save(u"d:\\职位.xlsx")
#
#
# if __name__ == "__main__":
#     main()
from lianxi.test1 import aa
print(aa)
print(list(map(aa,["a"])))