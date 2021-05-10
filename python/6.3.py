# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:03:04 2021

@author: sh010
"""

class Node:
    def __init__(self,elem, link = None):
        self.data = elem
        self.link = link
class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self): return self.front == None
    def clear(self): self.front= None
    
    def size(self):
        node = self.front
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count
    
    def display(self, msg='LinkedList'):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while node.link != None:
                print(node.data, end ="->")
                node = node.link
            print(node.data)
        else: 
            print("비어있습니다")
        
    def getNode(self, pos):
        if pos < 0 : return None
        node = self.front
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
        node = self.front
        while node is not None:
            if node.data == data : return node
            node = node.Link
        return node
    
    def insert(self, elem):
        node = Node(elem, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.link = node
            self.rear = node
        
    def delete(self):
        if not self.isEmpty():
            if self.rear == self.front:
                self.front = None
            else:
               self.front = self.front.link
               

s = LinkedList()
n = int(input("노드의 개수 : "))
for i in range(n):
    data = input(f"노드#{i+1} 데이터 : ")
    s.insert(data)

s.display("생성된 연결 리스트: ")
s.delete()
s.delete()
s.delete()
s.display("delete 연산 3번 실행 후 생성된 연결 리스트: ")