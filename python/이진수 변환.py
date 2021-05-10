# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:51:46 2021

@author: sh010
"""

class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


s = Stack()
n = 4096
while n >0 :
    s.push(n%2)
    n = n // 2
while not s.isEmpty():
    print(s.pop(), end ='')
print()
