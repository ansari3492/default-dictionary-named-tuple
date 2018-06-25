# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:49:44 2018

@author: Lenovo
"""
from string import ascii_lowercase as asc
kst4 = ["_","-"]


str1=input()
lst = str1.split("@")


if lst[0].isalnum() or  "_" in lst[0] or "-" in lst[0]:
    lst1 = lst[1].split(".")
    if lst1[0].isalnum() :
        if len(lst1[1]) == 3:
            print ("valid email")
        else:
            print("invalid email")
    else:
        print("invalid email")
else:
        print("invalid email")
