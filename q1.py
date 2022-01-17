#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:15:23 2021

@author: berkayakdag
"""

"""
The students took 2 exams. The user will enter both grades. 
First exam will have the percentage of 35%, and the second one will have 65%. 
If the student exeeds 80 on both exams. 5 points will be added after the total grades.
"""

exam1 = int(input("Enter the first exam grade: "))
exam2 = int(input("Enter the second exam grade: "))

total = exam1 * 0.35 + exam2 * 0.65

if total > 80:
    total += 5
    print("Your total grade is: ", total, "\nYou got 5 extra points.")
else:
    print("Your total grade is: ", total)

