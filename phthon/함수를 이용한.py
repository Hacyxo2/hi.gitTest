# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:35:51 2021

@author: sh010
"""

items = []
def insert(pos, elem):
    items.insert(pos, elem)
def delete(pos):
    return items.pop(pos)
def getEntry(pos):
    return items[pos]

def isEmpty():
    return len(items) == 0
def size():
    return len(items)
def clear():
    global items
    items = []
def find(item):
    return items.index(item)
def replace(pos, elem):
    items[pos] = elem
def sort():
    items.sort()
def merge(lst):
    items.extend(lst)
def display(msg='ArrayList:'):
    print(msg, size(), items)

a = [30, 60, 10, 40, 20, 50]
items = a
print(a)