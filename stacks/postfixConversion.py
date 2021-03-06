#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:10:01 2020

@author: don_quixote
"""

from stacks import Stack


def infix_to_postfix(infix_exp):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_exp.split()
    
    for token in token_list:
        if token in"ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while token != ')':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
        
    return " ".join(postfix_list)


print(infix_to_postfix("( A + B ) * C - ( D - E )  * ( F + G )"))