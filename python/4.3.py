# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:30:37 2021

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


def checkBracketsV2(lines):
    stack = Stack()
    for line in lines:
        if line in ('{', '[', '('):
            stack.push(line)
        elif line in ('}', ']', ')'):
            if stack.isEmpty():
                return '조건 2 위반', line
            else:
                left = stack.pop()
                if (line == "}" and left != "{") or \
                   (line == "]" and left != "[") or \
                   (line == "(" and left != ")"):
                    return '조건 3 위반', line
    if not stack.isEmpty():
        return '조건 1 위반', stack.top
    return 0


j = 1 #라인수 체크
c = 0 #괄호 에러 체크
filename = "4.1.py"
for i in filename:
    if "py" in filename:
        infile = open(filename,"r",encoding=('UTF8'))
lines = infile.readlines() 
for s in lines:
    checkBracketsV2(s)
    result = checkBracketsV2(s)
    if result != True:
        print(f'{filename} ---> 라인 {j} 문자 {result}')  
        c += 1
    j += 1
if c == 0:
    print(filename, "--->", result)
infile.close()