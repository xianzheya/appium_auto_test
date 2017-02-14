# -*- coding:utf-8 -*-

from server.appium_server import appiumDriver as ad


class shouyePage(object):
    
    #首页的最下面的首页按钮
    shouyeElement = "com.mqunar.atom.alexhome:id/atom_alexhome_home_default"
    
    #首页最近关注
    zuijinguanzhu = "com.mqunar.atom.alexhome:id/atom_alexhome_card_title_single_line_container"
    
    #首页您可能想去
    ninkennegxiangqu = "com.mqunar.atom.alexhome:id/atom_alexhome_card_title_single_line_container"
    
    #首页热门目的地
    mudidi = "com.mqunar.atom.alexhome:id/atom_alexhome_card_title_single_line_container"
    #首页热门专题
    zhuanti = "com.mqunar.atom.alexhome:id/atom_alexhome_card_title_single_line_container"
    def __init__(self):
        self.__driver = ad.appium_driver
    def get_loction(self):
        lo = self.__driver.find_element_by_id(self.shouyeElement)
        # 获取元素左上角的坐标
        print(lo.location)
        #元素的大小和位置的字典
        # print(lo.rect)
        #获取元素的大小
        print(lo.size)
        #截图
        # self.__driver.save_screenshot("xz.jpg")
        r = self.__driver.page_source
        # print(r)
        # print(type(r))
        # self.__driver.get_screenshot_as_png()
        # print(self.__driver.window_handles)
        #获取当前的页面网址
        # print(self.__driver.current_url)
        with open("p.xml", "w", encoding="utf-8") as f:
            f.write(r)

    def stop(self):
        self.__driver.quit()

        
if __name__ == '__main__':
    s = shouyePage()
    s.get_loction()
    s.stop()