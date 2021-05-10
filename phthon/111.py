# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:38:21 2021

@author: sh010
"""

def palindrome(a, b):
    s = Stack()
    t = Stack()
    a = a.upper()
    b = b.upper()
    for term in a:
        if term not in ' ':
            s.push(term)
        