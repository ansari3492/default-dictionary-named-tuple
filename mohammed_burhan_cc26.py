# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:02:54 2018

@author: Lenovo
"""

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    
    d[item] = d.get(item, 0) + int(quantity)
    print(d[item])
for item, quantity in d.items():
    print(item, quantity)