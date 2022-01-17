#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:34:08 2021

@author: berkayakdag
"""

"""
Ask a number from the user, then divide that number to 2. 
Then check both numbers if they are even or odd. 
Print the result. 

"""

num = int(input("Enter a number: "))

if num %2 == 0 and num/2 %2 == 0: 
    print("The numbers", num,"and", num/2 , "are both even.")
    
elif num%2 == 0 and num/2 %2 == 1:
    print("The number", num," is even and the number", num/2, "is odd.")

elif num%2 == 1 and num/2 %2 == 0:
    print("The number", num," is odd and the number", num/2, "is even.")

else: 
    print("The numbers",num, "and", num/2, "are both odd.")
    
    
    