#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:23:30 2020

@author: don_quixote
"""


""" binary seach work with only sorted list  in this rather than checking 
all the items we check for item at the mid point and make decion accordingly
which side of the list to search for the item,
the time complexty of of binary search is O(logn)"""

def BinarySearch(theList, key):
    first = 0
    last = len(theList) - 1
    """ here we are using first and last  index to find the midpoint of the list"""
    """ so we have 3 cases here  we would get the list at the midpoint or it would
    be present somewhere in the left or the right side of the list
    since we have a sorted list over here,so if the value is not present at
    the mid point we would check if the value is more than or less than the mid 
    and accordingly look for the value"""
    found = False
    
    while first <= last and not found:
        midpoint = (first + last)//2
        if theList[midpoint] == key:
            found = True
        else:
            if key < theList[midpoint]:
                last = midpoint - 1
            else: 
                first = midpoint + 1
    return found
theList = [1,2,4,5,6,7,7,8,12,56,78,90]
print(BinarySearch(theList, 12))
print(BinarySearch(theList, 100))
    