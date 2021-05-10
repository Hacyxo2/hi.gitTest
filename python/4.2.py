# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:27:58 2021

@author: sh010
"""

"""회문"""

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
        
    def reverse(self): 
        a = Stack()
        while len(self.top) > 0:
            a.push(self.pop())
        return a
        
def palindrome(string):
    s = Stack()
    t = Stack()
    string = string.upper()
    check = 0
    for term in string:
        if term not in ' ':
            if term not in ",.:;'"'"'"":
                s.push(term)
                t.push(term)
    b = t.reverse()
    c = s.size()
    print(f'{s.top}\n{b.top}')                    
    for i in range(len(s.top)):
        if s.peek() == b.peek():
            s.pop()
            b.pop()
            check += 1
        else:
            check -= 1
            s.pop()
    if check == c:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")
        

string = str(input())

palindrome(string)