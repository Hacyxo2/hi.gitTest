# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:28:26 2021

@author: sh010
"""

class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top =[]

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == "(" and left != ")"):
                    return False

    return stack.isEmpty()


str = ("{ A[(i+1)] = 0; }", "if((i==1)&&(j==0))", "A[ (i+1] ) = 0;")
for s in str:
    m = checkBrackets(s)
    print(s, "--->", m)