#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:02:25 2020

@author: don_quixote
"""


from stacks import Stack

def conversion(num , base):
    digits = "0123456789ABCDEF"
    
    rem = Stack()
    
    while num > 0:
        rem.push(num % base)
        num = num // base
        
        
    num_string = ""
    while not rem.is_empty():
        num_string = num_string + digits[rem.pop()]
    return num_string

print(conversion(25, 2))
print(conversion(25, 16))
    