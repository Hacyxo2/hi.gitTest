# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:56:32 2021

@author: sh010
"""

class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next
    
class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):return self.front == None
    def clear(self): self.front = self.front = None
    def size(self):
        
    def display(self, msg):
        