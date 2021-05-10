# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:25:18 2021

@author: sh010
"""

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i + 1, n):
            if(A[j] < A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1)

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged: break;
        printStep(A, n-i)
    
def printStep(arr, val):
    print(" Step %2d = "% val, end='')
    print(arr)
    
"""data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
selection_sort(data)
print("Selection : ", data)
print("_______________________")
data1 = [5,3,8,4,9,1,6,2,7]
print("Original : ", data1)
insertion_sort(data1)
print("Selection : ", data1)
print("_______________________")"""
data2 = [5,3,8,4,9,1,6,2,7]
print("Original : ", data2)
bubble_sort(data2)
print("Selection : ", data2)