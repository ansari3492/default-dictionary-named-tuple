# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:13:41 2018

@author: Lenovo
"""
n=input()

lst1 = n.split(" ")

for i in lst1:
    str_rev = i[::-1]
    if i == str_rev:
        print("True")
        break
   