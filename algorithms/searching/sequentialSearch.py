#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:09:59 2020

@author: don_quixote
"""


""" with searching we are able to find a perticular data from list of data 
from a array string or say the list(and  from other data types)"""

def linear_search(theList,item):
    pos = 0
    found = False
    """ sequancial search is also called linear search in this we 
    itearate over the list item one by one and look for the number to be found
    if it is available """
    
    while pos < len(theList) and not found:
        if theList[pos] == item :
            
            """ with if statement we are comparing item to be searched at every 
            index of the list and once its found it returns true as output"""
            found = True
        else:
            pos = pos + 1
            
    return found

llist = [1,3,5,4,6,6,5,4,5,3,3,3]
print(linear_search(llist , 6))
""" here we are passing the list and the number to be searched in the lsit"""
print(linear_search(llist, 7))
 