# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:09:37 2021

@author: sh010
"""

class Stack:
    def __init__(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    
    def isEmpty(self): return len(self.top) == 0

class Queue:
    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()
        
    def isEmpty(self): 
        if self.S1.isEmpty() and self.S2.isEmpty():
            return True
        else:
            return False
    # 입력이 들어오면 S1에 넣음
    def enqueue(self, item):
        self.S1.push(item)
    # 출력은 S2에서 수행 S2가 비어있으면 S1의 항목을 S2로 보낸다.    
    def dequeue(self):
        if self.isEmpty():
            return None
        if self.S2.isEmpty():
            for i in range(len(self.S1.top)):
                self.S2.push(self.S1.pop())
        return self.S2.pop()

q = Queue()

for i in range(6):
    q.enqueue(i)

while not q.isEmpty():
    print(q.dequeue(), end =' ')
