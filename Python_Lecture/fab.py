# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:08:20 2019

@author: YQW
"""

def fab(n):
    
    u_0 = 1;
    u_1 = 1;
    
    if n == 0:
        return u_0
    if n == 1:
        return u_1
    
    i = 1;
    while i < n:
        temp = u_1
        u_1 = u_1 + u_0
        u_0 = temp
        i = i + 1;
        
    return u_1;
        
print(fab(0))
print(fab(1))
print(fab(2))
print(fab(3))
print(fab(4))
print(fab(5))
    
    

