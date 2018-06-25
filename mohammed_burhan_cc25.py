# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:09:43 2018

@author: Lenovo
"""

list1 = []
while True:
    str1 = input()
    if not str1:
        break
    tup1 = str1.split(',')
    print (tup1)
    list1.append((tup1[0], int(tup1[1]), int(tup1[2])))
    
print(sorted(list1))
    
    

