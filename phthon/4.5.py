# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:54:03 2021

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

def precedence(op): # 우선순위 확인
    if op == '(' or op == ')': return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1

def evalPostfix(expr): # 후위표기 계산
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if(token =='+'): s.push(val1 + val2)
            elif(token =='-'): s.push(val1 - val2)
            elif(token =='*'): s.push(val1 * val2)
            elif(token =='/'): s.push(val1 / val2)
        else:
            s.push(float(token))
            
    return s.pop()

def Infix2Postfix(expr): #중위표기 후위표기 변환
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op =s.pop()
                if op=='(' : break
                else: output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else: output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    
    return ''.join(output) # 리스트를 문자열로 변환


infix = input('중위표기 수식을 입력하세요')
postfix = Infix2Postfix(infix)
result = evalPostfix(postfix)
print(' 중위표기: ', infix)
print(' 후위표기: ', postfix)
print(' 계산결과: ', result)