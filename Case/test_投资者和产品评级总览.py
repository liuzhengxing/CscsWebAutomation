# -*- coding: utf-8 -*-
import unittest
from Common.public_method import PublicMethod as PM
import Common.read_data as rd
page = "投资者和产品评级总览页面"

class TestPage1(unittest.TestCase):

    pm = PM()

    @classmethod
    def setUpClass(self):
        self.pm.open_browser()

    def setUp(self):
        self.pm.login()

    def testOne(self):
        self.pm.get_object(page,"投资者和产品评级总览").click()


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.pm.close_browser()

if __name__=='__main__':
    unittest.main()

