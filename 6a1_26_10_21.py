#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:59:08 2021

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

check = 0
for i in range (1,4):
    num = random.randint(1,10)
    guess = int(input("Enter a number: "))
    if num == guess:
        check += 1
    
if check == 1: 
    print("You have won 100 TL")
elif check == 2:
    print("You have won 25000 TL")
elif check == 3: 
    print("You have won 500000 TL")
else:
    print("You lose.")
    
    
