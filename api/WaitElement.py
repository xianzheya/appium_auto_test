# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import  WebDriverWait

def utilTure(dr,id,time=20):
    return WebDriverWait(dr,time).until(lambda x:x.find_element_by_id(id).is_displayed())