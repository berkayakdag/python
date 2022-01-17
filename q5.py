#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:54:04 2021

@author: berkayakdag
"""

"""
Create a "forgot my password" code.
The code will check if the new password is the same with the old password. 
If the previous and the current passwords are the same, the code will warn the user. 
If not, print the result. 
"""

password = 'Hello123'


newpass = input("Please enter your new password: ")
if password == newpass: 
    print("The password you have entered cannot be the same with the previous one.")
else: 
    print("Password changed...")
    

