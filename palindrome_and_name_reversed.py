#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:48:53 2022

@author: berkayakdag
"""
"""
def isPalindrome(s):
   
    if s == s[::-1]:
        return "palindrome"
    
    else:
        return "not palindrome"

s = "malayalam"

print(isPalindrome(s))
"""
def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ',' + firstName)
    else:
        print(firstName, lastName)

printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse = False)
printName('Olga', lastName = 'Puchmajerova', reverse = False)
printName(lastName = 'Puchmajerova', firstName = 'Olga', reverse = False)
