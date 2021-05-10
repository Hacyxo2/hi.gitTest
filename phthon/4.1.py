# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:25:12 2021

@author: sh010
"""

class Stack:
    def __init__(self):
        self.top = []
        
    def isEmpty(self): return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        
    def reverse(self):
        a = Stack()
        while len(self.top) > 0:
            a.push(self.pop())
        return print(''.join(a.top)) # join함수로 스택을 문자열로 변경


string = input('문자열을 입력하세요 : ')
s = Stack()
for i in string:
    s.push(i)

s.reverse()
