# -*- coding: utf-8 -*-
import unittest
from Common.public_method import PublicMethod as PM
import Common.read_map as rm
import Common.read_data as rd
page = "普通投资者画像筛选页面"

class TestPage2(unittest.TestCase):

    pm = PM()

    @classmethod
    def setUpClass(self):
        self.pm.open_browser()

    def setUp(self):
        self.pm.login()

    def testOne(self):
        self.pm.get_object(page,"普通投资者画像筛选").click()
        assert True == self.pm.get_object(page,"投资者").is_displayed()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.pm.close_browser()

if __name__=='__main__':
    unittest.main()

