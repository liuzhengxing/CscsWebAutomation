# -*- coding: utf-8 -*-
import unittest

class A():
    def A1(self):
        self.a1 = 0

    def A2(self):
        print(self.a1)

a = A()
a.A1() #必须先调一下A1函数，给a1赋值
a.A2()

class B(unittest.TestCase):

    b = A()

    def setUp(self):
        self.b.A1() #必须先调一下A1函数，给a1赋值


    def test1(self):
        self.b.A2()

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()

def C():
    c1 = 1
    c2 = 2
    return c1,c2
c = C()
print(c)