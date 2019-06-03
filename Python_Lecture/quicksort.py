# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:13:50 2019

@author: YQW
"""

def __partition(arr,left,right):
    v = arr[left]
    p = left;
    i = left + 1
    while True:
        if arr[i] < v:
            c        = arr[p+1];
            arr[p+1] = arr[i]
            arr[i]   = c
            p        = p + 1
            
        i = i + 1
        if i > right:
            break
        
    c         = arr[left];
    arr[left] = arr[p];
    arr[p]    = c;
        
    return p

def __quickSort(arr,left,right):    
    if left >= right:
        return     
    # partition
    pp = __partition(arr,left,right)
    # digui sort 
    __quickSort(arr,left,pp-1)
    __quickSort(arr,pp+1,right)
    
def quickSort(arr):
    length = len(arr)
    __quickSort(arr,0,length-1)
    return 

a = [1,4,5,3,2]
quickSort(a)
print(a)
