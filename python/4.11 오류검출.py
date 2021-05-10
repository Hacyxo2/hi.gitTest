# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:32:49 2021

@author: sh010
"""
import sys
top = []


def isEmpty():
    return len(top) == 0


def push(item):
    top.append(item)


def pop():
    if isEmpty():
        print("error")
        sys.exit()
    else:
        return top.pop(-1)


def peek():
    if isEmpty():
        print("error")
        sys.exit()
    else:
        return top[-1]


def size(): return len(top)


def clear():
    global top
    top = []


for i in range(1, 6):
    push(i)
print('push 5회: ', top)
print('pop() --> ', pop())
print(8%8)
print('pop() --> ', pop())
print('pop() --> ', pop())
print('pop() --> ', pop())
print('pop() --> ', pop())
print('pop() --> ', peek())
print('pop 2회: ', top)

