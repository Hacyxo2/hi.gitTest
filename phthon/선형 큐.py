# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:23:51 2021

@author: sh010
"""

items = []
def isEmpty():
    return len(items) == 0
def enqueue(item):
    items.append(item)
def dequeue():
    if not isEmpty():
        return items.pop(0)
def peek():
    if not isEmpty(): return items[-1]