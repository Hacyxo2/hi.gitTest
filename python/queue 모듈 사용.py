# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:41:27 2021

@author: sh010
"""

import queue
Q = queue.Queue(maxsize = 20)
for v in range(1,10):
    Q.put(v)
print("큐의 내용: ", end='')
for _ in range(1, 10):
    print(Q.get(), end=' ')
print()
