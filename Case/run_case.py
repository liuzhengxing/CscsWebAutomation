# -*- coding: utf-8 -*-
import unittest
import time
import sys
sys.path.append('C:\Users\liuzx\PycharmProjects\CscsWebAutomation')
from Common import HTMLTestRunnerCN
from pathlib import Path

#取当前工作路径
BaseDir = Path.cwd()

# 定义测试集
testunit=unittest.TestSuite()

# 定义case文件所在的路径
test_dir = BaseDir

#使用discover方法找到所有以test开头的python文件
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py",
                                             top_level_dir = None)

#循环查找python文件，把所有的case添加到测试集中
for test_suite in discover:
    for test_case in test_suite:
        testunit.addTest(test_case)

#取系统时间和报告title
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
title = '适当性UI自动化测试报告' + now

#定义报告问存放路径并生成报告
report_dir = BaseDir / '../Report'
file = report_dir/ (title + '.html')
fp = open(file,'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=title, description=u'用例执行情况：')

#执行测试集
runner.run(testunit)
