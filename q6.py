#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:59:30 2021

@author: berkayakdag
"""

"""
Extend the "forgot my password" code. 
Check for the password the user enters. 
If the password is not the same with the password stored in the code, 
the user will have to change the password.
"""

password = 'Hello123'

userpass = input("Enter your password: ")
if userpass == password: 
    print("Hello user.")
else: 
    newpass = input("Please enter your new password: ")
    if password == newpass: 
        print("The password you have entered cannot be the same with the previous one.")
    else: 
        print("Password changed...")
        
