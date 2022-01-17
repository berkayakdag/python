#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:38:21 2021

@author: berkayakdag
"""
"""
User deposits money, if the user enters 0, print the total. 
while
Enter amount: 100 
Enter amount: 50
Enter amount: 75
Enter amount: 0

225

"""





res = 0
money = int(input("Enter amount: "))
res = money

while money != 0:
    money = int(input("Enter amount: "))
    res += money

print(res)

