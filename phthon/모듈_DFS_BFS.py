# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:49:38 2021

@author: sh010
"""

import queue
"""너비 탐색"""  
Q = queue.Queue(maxsize=6)

def isValidPos(x,y):
    if x < 0 or y < 0 or x >= Q.maxsize or y >= Q.maxsize:
        return False
    else:
        return qmap[y][x] == '0' or qmap[y][x] == 'x'
  
def BFS():
    que = queue.Queue()
    que.put((0,1))
    print('BFS: ')
    
    while not que.empty():
        here = que.get()
        print(here, end='->')
        (x, y) = here
        if(qmap[y][x]=='x'):
            return True
        else:
            qmap[y][x] = '.'
            if isValidPos(x, y - 1): 
                que.put((x, y - 1))
            if isValidPos(x, y + 1): 
                que.put((x, y + 1))
            if isValidPos(x - 1, y): 
                que.put((x - 1, y))
            if isValidPos(x + 1, y): 
                que.put((x + 1, y))  
    return False
                
qmap = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]

"""깊이 탐색"""    
S = queue.LifoQueue(maxsize = 6)
    
def isValidPos1(x,y):
    if x < 0 or y < 0 or x >= S.maxsize or y >= S.maxsize:
        return False
    else:
        return smap[y][x] == '0' or smap[y][x] == 'x'
                            
def DFS():
    stack = queue.LifoQueue()
    stack.put((0, 1))
    print('DFS: ')
    
    while not stack.empty():
        here = stack.get()
        print(here, end='->')
        (x, y) = here
        if(smap[y][x] == 'x'):
            return True
        else:
            smap[y][x] = '.'
            if isValidPos1(x, y - 1):
                stack.put((x, y - 1))
            if isValidPos1(x, y + 1):
                stack.put((x, y + 1))
            if isValidPos1(x - 1, y):
                stack.put((x - 1, y))
            if isValidPos1(x + 1, y):
                stack.put((x + 1, y))
    return False

smap = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]


result = BFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')

result1 = DFS()
if result1 : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')s

