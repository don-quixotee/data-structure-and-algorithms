#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:19:35 2020

@author: don_quixote(Abhishek singh)

"""

"""in python stacks are implemented using list
we can create a class to defilne the stack operation and import 
it in any programs to  to use it"""

class Stack:
    
    def __init__ (self):
        self.items = []
        """an empty list for the stack operation"""
    def is_empty(self):
        return self.items == []
        """this will return true if the list is empty """
    def push (self,item):
        self.items.append(item)
        """this adds an element at the end of the stack"""
    def pop(self):
        return self.items.pop()
    """#removes the last in elements of the list"""
    def peek(self):
        return self.items[len(self.items)-1]
    """#returns the last element from the
       #stack without removing it"""
    def size(self):
        return len(self.items)
    """ this will return the size of the stack we created """