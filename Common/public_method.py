# -*- coding: utf-8 -*-

from selenium import webdriver
from Common import read_data as rd
from Common import read_map as rm

class PublicMethod():

    # 指定浏览器类型为chrome，并打开浏览器，输入url
    def open_browser(self):
        self.browser = webdriver.Chrome("D:\Tools\chromedriver_win32\chromedriver")
        self.browser.implicitly_wait(30)
        self.browser.get(rd.read_data("url"))
        self.browser.maximize_window()

    # 关闭当前浏览器所有的tab，有别于browser.close()方法
    def close_browser(self):
        self.browser.quit()

    # 1.根据传入的page和mapKey，返回对应页面元素的类型和value的组合，返回的是一个tuple
    # 2.根据元素类型和value，返回找到页面的方法
    # 3.暂时注释掉if... else方法，用python自带的字典来实现switch case循环判断
    # 4.把函数名放入字典，默认取的是None
    def get_object(self, page, mapKey):
        group = rm.read_map(page, mapKey)
        # if "xpath" in self.value[1]:
        #     return self.browser.find_element_by_xpath(self.value[0])
        # elif "id" in self.value[1]:
        #     return self.browser.find_element_by_id(self.value[0])
        s = {
            "xpath":self.browser.find_element_by_xpath,
            "id": self.browser.find_element_by_id,
            "name": self.browser.find_element_by_name
        }
        return s.get(group[1], None)(group[0])

    def login(self):
        self.get_object("登录页面","用户名").send_keys(rd.read_data("用户名"))
        self.get_object("登录页面","密码").send_keys(rd.read_data("密码"))
        self.get_object("登录页面","验证码").send_keys(rd.read_data("验证码"))
        self.get_object("登录页面","登录").click()
        assert rd.read_data("title") == self.browser.title

    # 1.该方法封装了selenium的send_keys方法，根据get_object方法找到页面元素
    # 2.根据dataKey，找到data文件中的具体值
    # 3.通过send_keys方法，在页面元素中输入具体的值
    def input_data(self, page, mapKey, dataKey):
        self.inputBox = self.get_object(page, mapKey)
        self.data = rd.read_data(dataKey)
        self.inputBox.send_keys(self.data)

    def logout(self):
        pass

