# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:38:27 2021

@author: sh010
"""

def find_max_min(A):
    fmax = A[0]
    fmin = A[0]
    for i in A:
        if i > fmax:
            fmax = i
    for i in A:
        if i < fmin:
            fmin = i
    return (fmax, fmin)


A = [30, 60, 40, 20, 10]

(x) = find_max_min(A)
print("(min,max) = ", x)