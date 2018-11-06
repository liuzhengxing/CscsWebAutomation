# -*- coding: utf-8 -*-
import unittest
from Common.public_method import PublicMethod as PM
import Common.read_map as rm
import Common.read_data as rd
page = "适当性风险监测页面"

class TestPage3(unittest.TestCase):

    pm = PM()

    @classmethod
    def setUpClass(self):
        self.pm.open_browser()

    def setUp(self):
        self.pm.login()

    def testOne(self):
        self.pm.get_object(page,"适当性风险监测").click()
        self.pm.get_object(page, "查看具体产品").click()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
        # self.pm.close_browser()

if __name__=='__main__':
    unittest.main()

