# -*- coding: utf-8 -*-

class A():

    def fooA(self):
        self.a = 100
        self.b = 101

    def fooB(self):
        b = 102

        c1 = b + 1

        c2 = self.b + 1

        print(c1)
        print(c2)

a = A()
a.fooA()
a.fooB()
