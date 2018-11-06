# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from Common import read_map as rm

def getObject(a,*args):
    if args == ():
        return "find by xpath"
    elif "id" in args:
        return "find by id"
    elif "name" in args:
        return "find by name"


def readMap(page, key):
    filePath = "../Map/map_QA"
    file = open(filePath, encoding='utf-8')
    text = json.load(file)
    value = text[page][key]["value"]
    file.close()
    return value


result = getObject("xpathvalue","id")

# print(result)


def get_object(page,key):
    value = rm.read_map(page,key)
    s = {
        "xpath":"browser.find_element_by_xpath(value[0])",
        "id":"browser.find_element_by_id(value[0])"
    }
    return s.get(value[1],"OK")


print(get_object("登录页面","用户名"))