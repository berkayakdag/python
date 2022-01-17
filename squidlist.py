#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:28:04 2021

@author: berkayakdag
"""

"""
Create a challenge of 5 games, there will be x person,
(10A1 and A2 students + Berkay) list their names 



In every game, random 3 students will be deleted from the list RANDOM.
After every game, remaining players will be on the same list and printed out. 

Random person will be picked from the list and the winner will be printed out. 

Hint: use list1.remove() and random.choice()
"""


list1 = ["Berkay", "", "", ]

for 5:
    for 3: 
        list1.remove random.choice()
    print()
print()
























import random

list1 = ["Berkay", "Ömer", "Deniz", "Kuzey", "Naz", "İdil", "Zeren", "Berra", "Güneş"," Okan", "Aras", "Tolga",
         "Ege", "Bera", "Göktuğ","Beren Naz", "Masal", "Nilsu", "Ulaş", "Beren", "Defne", "Arsım", "Güneş Ekin"]

for j in range (0,5):
    for i in range (0,3):
        list1.remove(random.choice(list1))
    print(list1)

print(random.choice(list1))

