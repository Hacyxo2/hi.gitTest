# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:49:54 2021

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

    def display(self):
        if len(self.top) > 0:
            print(self.pop(), end =" ")
            return self.display()
        

values = Stack()
for i in range(20):
    if i % 3 == 0:
        values.push(i)
    elif i % 4 == 0:
        values.pop()
print(values.top)

value = Stack()
for i in range(10):
    if i % 3 == 0:
        value.push(i)
print(value.top)