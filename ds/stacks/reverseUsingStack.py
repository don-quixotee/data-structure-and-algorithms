#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:52:16 2020

@author: don_quixote
"""

from stacks import Stack
""" import stacks imports the previously defined stack class """

def reverseString (my_string):
    reverse_str=""
    x=Stack()
    """ we are using variable x as a stack variable as object of the
    previously defined stack class"""
    for s in my_string :
        x.push(s)
    for item in range(x.size()):
        reverse_str=reverse_str+x.pop()
        
    return reverse_str
    
    
string='Abhishek'
print(reverseString(string))

