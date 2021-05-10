# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:15:39 2021

@author: sh010
"""

class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)
        
    def insert(self, elem):
        if elem not in self.items :
            self.items.append(elem)

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
    
    def propersubset(self, setB):
        if self.difference(setB).size() == 0:
            return print('setA는 setB의 진부분집합이다.')
        elif setB.difference(self).size() == 0:
            return print('setB는 setA의 진부분집합이다.')
        else:
            return print('setA, B는 진부분집합이 아니다.')
        

setA = Set()
setA.insert('1')
setA.insert('2')
setA.insert('3')
setA.insert('5')
setA.display('Set A')

setB = Set()
setB.insert('1')
setB.insert('2')

setB.insert('5')
setB.display('Set B')

setA.propersubset(setB)