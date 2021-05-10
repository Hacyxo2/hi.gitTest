# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:41:55 2021

@author: sh010
"""

class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        return self.items.pop(pos)

    def size(self):
        return len(self.items)

    def replace(self, pos, elem):
        self.items[pos] = elem

    def display(self, msg='ArrayList:'):
        print(msg, self.items)


s = ArrayList()
s.insert(0, 10)
s.display("insert(0, 10) : List: ")
s.insert(1, 20)
s.display("insert(1, 20) : List: ")
s.insert(0, 30)
s.display("insert(0, 30) : List: ")
s.insert(2, 40)
s.display("insert(0, 30) : List: ")
s.insert(s.size(), 50)
s.display("insert(size(), 50) : List: ")