# -*- coding: utf-8 -*-

import json

def read_data(value):
    file = open("../Data/data_QA", encoding='utf-8')
    text = json.load(file)
    data = text[value]
    file.close()
    return data
