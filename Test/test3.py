# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from selenium import webdriver
from Common import read_data as rd
from Common import read_map as rm
import time
import json
import Common.read_map as rm


class PublicMethod():

    def openBrowser(self):
        self.browser = webdriver.Chrome("D:\Tools\chromedriver_win32\chromedriver")
        self.browser.get(rd.read_data("url"))
        self.browser.maximize_window()

    def closeBrowser(self):
        self.browser.quit()

    def get_object(self,page,key):
        self.value = rm.read_map(page,key)
        if "xpath" in self.value[1]:
            return self.browser.find_element_by_xpath(self.value[0])
        elif "id" in self.value[1]:
            return self.browser.find_element_by_id(self.value[0])

    def login(self):
        self.input_data("登录页面","用户名","用户名")
        self.input_data("登录页面","密码","密码")
        self.input_data("登录页面","验证码","验证码")
        self.get_object("登录页面","登录").click()
        time.sleep(3)

    def input_data(self,page,mapKey,dataKey):
        self.inputBox = self.get_object(page,mapKey)
        self.data = rd.read_data(dataKey)
        self.inputBox.send_keys(self.data)

    def logout(self):
        pass

p = PublicMethod()
p.openBrowser()
p.login()

