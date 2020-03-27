#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:29:21 2020

@author: don_quixote
"""
 

from stacks import Stack

def checker(paren):
    s = Stack()
    balanced = True
    index = 0
    while index < len(paren) and balanced:
        symbol = paren[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
                    
        index = index +1
      
    if balanced and s.is_empty():
        return True
    else:
        return False
def matches(open,close):
    opens = "({["
    closes = ")}]"
    
    return opens.index(open) == closes.index(close)

print(checker('[[[{()}]]]'))