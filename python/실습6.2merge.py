# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:13:38 2021

@author: sh010
"""

class Node:
    def __init__(self,elem, link = None):
        self.data = elem
        self.link = link
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedList'):
        print(msg, end=' ')
        if not self.isEmpty():
            node = self.head
            while node.link != None:
                print(node.data, end ="->")
                node = node.link
            print(node.data)
        
    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data
    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem
    def find(self, data):
        node = self.head;
        while node is not None:
            if node.data == data : return node
            node = node.Link
        return node
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
            
    def merge(self, l):
        node = l.head
        before = self.getNode(self.size()-1)
        before.link = node
        l.clear()
        return l        
       
A = LinkedList()
for i in range(5):
    A.insert(i, i)
print("A의 길이는 ",A.size(),"이다.")
B = LinkedList()
for i in range(5):
    B.insert(i, i)
print("B의 길이는 ",B.size(),"이다.")
A.merge(B)
print("merge 연산 후: A의 길이는 ",A.size(),"이다.")
print("merge 연산 후: B의 길이는 ",B.size(),"이다.")
A.display()