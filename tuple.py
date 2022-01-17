#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:20:24 2021

@author: berkayakdag
"""

t1 = (1,2,3,4,5)
t2= ('six','seven','eight')
t3 = t1 + t2
print('t3 = ', t3)

t4 = (t2 * 3)
print('t4 = ', t4)

print('3rd element from the beginning = ', t3[2])
print('3rd element from the end = ', t3[2])

print('Slice elements from index 4 to 7 inclusive = ', t3[3:7])