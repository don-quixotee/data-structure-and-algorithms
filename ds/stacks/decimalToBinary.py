#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:49:20 2020

@author: don_quixote
"""

from stacks import Stack
""" import stack to import the class Stacks  from stacks module"""

def divideBy2(num):
    
    """ in this function we are gonna find  the binary of the given 
    argument by using the divide by 2 algorithm and concatenating and 
    reversing it remiders when we dived the given number the the
    function by 2"""
    rem = Stack()
    
    while num > 0:
        rem.push(num%2)
        num = num // 2
    binary_num = ""
    
    while not rem.is_empty():
       binary_num = binary_num + str(rem.pop())
       
    return binary_num

num=1253

print(divideBy2(num))