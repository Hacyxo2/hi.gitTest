# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 17:11:27 2021

@author: sh010
"""

items = []


def insert(pos, elem):
    lbuf = []
    if items == []:
        items.append(elem)
    elif items[pos] != None:
        for i in range(pos, len(items)):
            lbuf.append(items[i])
        for i in range(pos, len(items)):
            items.pop(-1)
        items.append(elem)
        for i in range(pos, len(lbuf)):
            items.append(lbuf[i])
              
def delete(pos):
    if len(items) == pos + 1:
        return items.pop(-1)
    else:
        lbuf = []
        for i in range(pos + 1, len(items)):
             lbuf.append(items[i])
        for i in range(pos, len(items)):
             items.pop(-1)
        for i in range(0, len(lbuf)):
            items.append(lbuf[i])
        return "List"

def display(msg = 'List'):
    print(msg, items,"\n")

def merge(lst): 
    for i in range(0, len(lst)): 
        items.append(lst[i])
    return items

def find(num):
    count = []
    for i in range(0, len(items)):
        if items[i] == num:
            count.append(i)
        else:
            continue
            
    return num, count


insert(0, 5)
insert(0, 4)
insert(0, 3)
insert(0, 2)
insert(0, 1)
display('insert : ')
delete(3)
display('delete : ')
A = [6, 7, 8]
merge(A)
display('merge : ')
print("(찾을 수, 찾는 수와 같은 인덱스)",find(1))