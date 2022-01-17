#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:25:41 2021

@author: berkayakdag
"""

print("Berkay Akdağ")
name = input("What is your name?: ")

age = int(input("What is your age?: "))
print("Our age difference is " , abs(27 - age))

"""
Ask a number from the user and do the calculation. 

The first number must be 3 digits. Check for it. (if check)(100-999)
Numbers division by 2, subtract 8, multiply 13. 
Then ask another number and divide the first number with the second number. 
Print the result.
"""

num = int(input("Enter a number: "))
if num <= 999 and num >= 100:
    calc = (num / 2 - 8) * 13
    num2 = int(input("Enter number 2 :"))
    res = calc / num2
    print(res)
else:
    print("Wrong")
    

