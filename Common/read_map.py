# -*- coding: utf-8 -*-

import json

#读取map文件，返回对象是一个tuple类型，包含value和type
def read_map(page,key):
    filePath = "../Map/map_QA"
    file = open(filePath, encoding='utf-8')
    text = json.load(file)
    value = text[page][key]["value"]
    type = text[page][key]["type"]
    file.close()
    return value,type









