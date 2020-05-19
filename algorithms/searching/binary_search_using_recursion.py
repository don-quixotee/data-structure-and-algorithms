#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:44:35 2020

@author: don_quixote
"""


def BinarySearch(A, key, low, high):
    if low>high:
        return False
    else: 
        mid = (low+high)//2
        
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return BinarySearch(A, key, low, mid-1)
        else:
            return BinarySearch(A, key, mid+1 , high)

        
A = [20,23,47,76,89,100]
bs = BinarySearch(A,  89, 0, len(A))
print("the element 89 is ", bs)       

        
        
        
        
        
        
        
        
        
        
        
        
        