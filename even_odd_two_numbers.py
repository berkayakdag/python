#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:39:08 2021

@author: berkayakdag
"""

number = int(input('Please Write A Number'))

dividednumber = number / 2

if number % 2 == 0 and dividednumber % 2 == 0:
    print('Both Numbers Are Even')
elif number % 2 == 1 and dividednumber % 2 == 0:
    print("One is even, one is odd")
elif number % 2 == 0 and dividednumber % 2 == 1:
    print("One is even, one is odd")
else:
    print('Both Numbers Are Odd')