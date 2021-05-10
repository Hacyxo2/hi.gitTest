# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:20:09 2021

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

    def size(self):
        node = self.head
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count
    
    def display(self, msg='LinkedList'):
        print(msg, end='')
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

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    def push(self, item):
         self.insert(self.size(), item)
         
    def delete(self):
        if not self.isEmpty():
            n = self.head
            self.head = n.link
    
    def sumdata(self):
        s = 0
        node = self.head
        while not node == None:
            s += int(node.data)
            node = node.link
        return s
    
    def findSum(self,elem):
        if not self.isEmpty():
            node = self.head
            count = 0
            while not node == None:
                if int(node.data) == elem:
                    count += 1
                node = node.link
            return count
        
s = LinkedList()
n = int(input("노드의 개수 : "))
for i in range(n):
    data = input(f"노드#{i+1} 데이터 : ")
    s.insert(i, data)
n = int(input("탐색할 값을 입력하시오: "))
print(f"{n}는 연결 리스트에서 {s.findSum(n)}번 나타납니다.")
#6.16 
#print(f"연결 리스트의 데이터 합: {s.sumdata()}")
#6.13
#s.display("생성된 연결 리스트: ")    
#6.15
# s.delete()
# s.display("첫 번째 노드 삭제 후 연결 리스트 : ")
# 6.14
# data = input("끝에 추가할 데이터: ")
# s.push(data)
# s.display("생성된 연결 리스트: ")


