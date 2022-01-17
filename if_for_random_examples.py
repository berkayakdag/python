#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:27:07 2021

@author: berkayakdag
"""

"""
Random guessing game
Create a random number from 1-10.
The user will try to guess the number
Random number will be changed 3 times
If the user finds the correct number 1 time -> 100 TL
2 times -> 25000TL
3 times -> 500000TL
"""

import random 

count = 0

for i in range(1,4):
    num = random.randint(1,10)
    tahmin = int(input("Enter a number: "))
    
    if num == tahmin:
        count +=1

if count ==1:
    print("100 TL")
elif count == 2:
    print("25000TL")
elif count ==3:
    print("500000TL")
else:
    print("no")
    
    
    