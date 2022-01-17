#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:23:53 2021

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
    tahmin = int(input(""))
    if num == tahmin:
        count+=1

if count == 1:
    print("100 TL")
elif count == 2:
    print("25000TL")
elif count == 3:
    print("500000TL")
else:
    print("You lose")

"""
Harf notu hesaplama 

A 96 - 100
A-  90 - 96
B+ 84 - 90
B  78 - 84
B- 70 - 78
C+ 66 - 70
C 60 - 66
C- 52 - 60
D+ 45 - 52
D 40 - 45
F 0 - 40

"""

note = int(input("What is your grade: "))

if note > 96 and note <100:
    print("A")
elif note > 90 and note < 96:
    print("A-")
elif note > 84 and note < 90:
    print("B+")
elif note > 78 and note < 84:
    print("B")
elif note > 70 and note < 78:
    print("B-")
elif note > 66 and note < 70:
    print("C+")
elif note > 60 and note < 66:
    print("C")
elif note > 52 and note < 60:
    print("C-")
elif note > 45 and note < 52:
    print("D+")
elif note > 40 and note < 45:
    print("D")
elif note > 0 and note < 40:
    print("F")
else: 
    print("Invalid value.")
    