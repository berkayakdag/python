#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:12:21 2021

@author: berkayakdag
"""

"""

Deposit & Widthdraw

The balance is 1000

The program will ask Deposit or Widthdraw
If the user enters deposit, ask Enter amount: and sum the balance with the entered amount. 
If the user enters widthdraw, 
do the reverse


else, print Invalid. 


"""
balance = 1000

question = input("Deposit or widthdraw: ")

if question == "deposit":
    money = int(input("Enter amount: "))
    print(balance + money)
elif question == "deposit":
    money = int(input("Enter amount: "))
    print(balance - money)
else: 
    print("Invalid")























"""

balance = 1000

question = input("Deposit or widthdraw: ")
if question == 'deposit':
    money = int(input("Enter amount:"))
    print(balance + money)
elif question == 'widthdraw':
    money = int(input("Enter amount: "))
    print(balance - money)
else: 
    print("Invalid. ")
    