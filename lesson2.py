#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:36:14 2021

@author: berkayakdag
"""

"""
print("Berkay")

name = input("What is your name: ")
age = int(input("What is your age: "))
water = float(input("How much water do you drink: "))

print("Nice to meet you," , name , "your", age, "is great and drinking", water , "litres of water is enough.")
"""


"""
water = float(input("How much water do you drink in litre: "))

if water < 2:
    print("Drinking", water, "of water is not enough. You need to drink more to survive or you will end up in hospital or go to jail")
elif water > 40:
    print("Drinking", water, "of water is destroying our natural resources. Please stop and get some help. YOU ARE GOING TO BURST OUT!!! STOOOOOPPPPP!!!!!")
else:
    print("Aferin sana")
"""

"""
num1 = int(input("Enter number1: ")) 
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: ")) 

res = num1 + num2 + num3

print(res)



res = 0
for i in range (1,11):
    
    num = int(input("Enter a number: "))
    res += num
    
print(res)
"""


"""
Flip a coin 

Ask the user if the coin is heads or tails, 
if tails print win
else if heads print lose


hidden answer: if the user types straight,
print -> you won 50 krş
"""

coin = input("Heads or tails: ")
if coin == 'heads':
    print("Win")
elif coin == 'tails':
    print("Lose")
elif coin == 'straight':
    print("You won 50 krş")
else:
    print("Invalid option")
    
    
    




