#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:41:29 2021

@author: berkayakdag
"""

"""
Question:
    Write your name and ask the user his/her name,
    Ask the user his/her age and find the age difference from your age. (Our age difference is ...)
    
"""
print("Berkay Akdağ")
name = input("Enter your name: ")

age = int(input("Enter your age: "))
print("Our age difference is", abs(27 - age))





"""
Ask a number from the user and do the calculation. 

The first number must be 3 digits. Check for it. (if check)(100-999)
Numbers division by 2, subtract 8, multiply 13. 
Then ask another number and divide the first number with the second number. 
Print the result.

"""

num = int(input("Enter number 1: "))

if num > 99 and num < 1000:
    calc = ( num / 2 - 8 ) * 13
    num2 = int(input("Enter number 2: "))
    res = calc / num2
    
    print(res)
    
    
    
    
    
    
    
    
    