# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:52:38 2021

@author: sh010
"""
def SListC(A, B):
    c = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                c += 1
            else:
                continue
   
    return print(bool(c), c,'개 일치합니다.')


A = (input('리스트 A를 입력하세요: ').split())
B = (input('리스트 B를 입력하세요: ').split())
C = (input('리스트 C를 입력하세요: ').split())

SListC(A, B)
SListC(A, C)