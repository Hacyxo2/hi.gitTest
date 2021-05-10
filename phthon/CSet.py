# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:25:10 2021

@author: sh010
"""

class Set:
    def __init__(self):
        self.items = []

    def __sub__(self, B):
        return self.difference(B)

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)
    
    def contains(self, item):
        i = 0
        while i < len(self.items):
            if self.items[i] == item:
                return True
            i += 1
        return False
    
    def insert(self, elem):
            if self.contains(elem) != True:
                self.items.append(elem)
    
    def delete(self, elem):
        if self.contains(elem) == True:
            self.items.pop(elem)
    
    def union(self, B):
        setC = Set()
        setC.items = list(self.items)
        i = 0
        while i < len(B.items) :
            if self.contains(B.items[i]) != True :
                setC.items.append(B.items[i])
            i += 1
        return setC
    
    def intersect(self, B):
        setC = Set()
        i = 0
        while i < len(B.items) :
            if self.contains(B.items[i]) == True :
                setC.items.append(B.items[i])
            i += 1
        return setC
    
    def difference(self, B):
        setC = Set()
        i = 0
        while i < len(self.items) :
            if B.contains(self.items[i]) != True :
                setC.items.append(A.items[i])
            i += 1
        return setC
    
    def isSubsetOf(self, setB):
        if self.difference(setB).size() == 0 or self.intersect(setB) == self.items:
            return print('Subset는 Otherset의 부분집합이다.')
        else:
            return print('Subset, Otherset는 부분집합이 아니다.')

A = Set()
A.insert(1)
A.insert(2)
A.insert(3)
A.insert(4)
A.insert(5)
A.display("SetA : ")

B = Set()
B.insert(2)
B.insert(3)
B.insert(4)
B.insert(5)
B.display("SetB : ")

A.union(B).display('A U B : ')
A.intersect(B).display('A ^ B : ')
A.difference(B).display('A.difference(B) : ')

C = A - B
C.display('A - B : ')
A.display("SetA : ")

A.isSubsetOf(B)
B.isSubsetOf(A)