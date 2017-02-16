# -*- coding:utf-8 -*-

from server.appium_server import appiumDriver as ad
from time import sleep
from api.WaitElement import utilTure


class Action(object):
    def __init__(self):
        self.driver = ad.appium_driver
        s = self.driver.find_elements_by_class_name("android.widget.FrameLayout")[1]
        s_size = s.size
        s_location = s.location
        s_window = self.driver.get_window_size()
        if s_size["height"] + s_location["y"] == s_window["height"]:
            self.x = s_size["width"]
            self.start_y = s_location["y"]
            self.end_y = s_window["height"]
        else:
            self.x = s_size["width"]
            self.start_y = s_location["y"]
            self.end_y = s_window["height"] - (s_window["height"] - s_size["height"] - s_location["y"])

    # def click(self):
    #         self.driver.drag_and_drop()

    # 向下上滑动三分之一
    @property
    def swipe_up_three(self):
        x = self.x / 2
        y_start = (self.end_y - self.start_y) / 3 * 2
        y_end = (self.end_y - self.start_y) / 3 * 1
        self.driver.swipe(x, y_start, x, y_end)

    # 向上滑动二分之一
    @property
    def swipe_up_two(self):
        x = self.x / 2
        y_start = (self.end_y - self.start_y) / 6 * 4
        y_end = (self.end_y - self.start_y) / 6 * 1
        self.driver.swipe(x, y_start, x, y_end)

    # 滑动一屏
    @property
    def swipe_up_one(self):
        height = self.driver.find_element_by_id("com.mqunar.atom.alexhome:id/atom_alexhome_tab_indicator").size["height"]
        x = self.x / 5
        y_start = self.end_y - height - 1
        y_end = self.start_y
        self.driver.swipe(x, y_start, x, y_end)

    # 任意滑动
    def swip_up(self, start_x=None, start_y=None, end_x=None, end_y=None, time=None):
        if start_x is None or start_y is None or end_x is None or end_y is None:
            raise ValueError("请输入合适的值")
        elif self.end_y > start_y > self.start_y  or self.end_y > end_y > self.start_y:
            self.driver.switch_to(start_x, start_y, end_x, end_y, time)
        else:
            raise ValueError("请输入合适的值")

    # 向下滑动三分之一
    @property
    def swipe_down_three(self):
        x = self.x / 2
        y_start = (self.end_y - self.start_y) / 3
        y_end = (self.end_y - self.start_y) / 3 * 2
        self.driver.swipe(x, y_start, x, y_end)

    # 向下滑动二分之一
    @property
    def swipe_down_two(self):
        x = self.x
        y_start = (self.end_y - self.start_y) / 6
        y_end = (self.end_y - self.start_y) / 6 * 4
        self.driver.swipe(x, y_start, x, y_end)

    # 向上滑动一屏
    @property
    def swipe_down_one(self):
        height = self.driver.find_element_by_id("com.mqunar.atom.alexhome:id/atom_alexhome_search_layout").size["height"]
        x = self.x / 2
        y_start = self.start_y + height + 1
        y_end = self.end_y - 1
        self.driver.swipe(x, y_start, x, y_end)

    def huadong_zuo(self):
        self.driver.find_element_by_id("com.mqunar.atom.alexhome:id/atom_alexhome_search_layout").get_attribute("text")

    def huadong_you(self):
        pass

    def changan(self,ele):
        pass

    def shuru(self,ele):
        pass

    def stop(self):
        self.driver.quit()


if __name__ == "__main__":
    a = Action()
    # print(Action.__dict__)
    try:
        for i in range(1):
            a.swipe_up_one
            print("up")
            # e = a.driver.find_elements_by_id("com.mqunar.atom.alexhome:id/atom_alexhome_small_entrance_card")
            # print(len(e))
            # print(e)
            # print(e.size,e.location)
            # f = e.find_elements_by_class_name("android.widget.LinearLayout")
            # print(len(f))
            # for i1 in f:
            #     print(i1.find_element_by_class_name("android.widget.TextView").text)
            #     print(i1.find_element_by_class_name("android.widget.TextView"))
            # s1 = a.driver.page_source
            # with open("x.xml", "w", encoding="utf-8") as f:
            #     f.write(s1)
            # a.swipe_down_one
            # print("down")
        # for i in range(3):
        #     a.swipe_up()
        #     print("up")
        # a.stop()
    except Exception as e:
        print(e)
        # a.stop()
    finally:
        a.stop()
        # pass
