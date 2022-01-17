#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:33:07 2021

@author: berkayakdag
"""

"""
Q1. Ask the user his/her name, age, birthplace and favourite number. 

If the number is less than 50, do the calculation.


num . 47     477
--------- - ----- + 42
   16         4
   
If the number is more than 50, do the calculation. 

num : 12 - 10 . 58 - 200

"""
name = input("What is your name: ")
age = int(input("How old are you: "))
birth = input("Where did you born: ")
num = int(input("What is your favourite number: "))

if num < 50: 
    print((num * 47 / 16) - (477 / 4) + 42)
elif num > 50: 
    print(num / 12 - 10 * 58 - 200)
else: 
    print("Num is 50")

"""
Q2. 
Weather and prize code. 

The user will enter todays temperature in celcius. 

If it is less than 10, suggest him/her to take a jacket. 
If it is more than 10, suggest him/her to take sunglasses. 

Ask the user a number from 1 to 10. 

From 1 to 10, for every number give a prize to the user. 
Ex: 
1 = car
2 = smartphone
.
.
.

"""

weather = int(input("Whats the weather today in celcius: "))
if weather < 10: 
    print("Wear a jacket.")
else: 
    print("Take sunglasses")
    
num = int(input("Enter a number: "))

if num ==1 : 
    print("car")
elif num == 2:
    print("smartphone")
elif num ==3:
    print("lahmacun")
elif num == 4:
    print("tabak")
elif num == 5: 
    print("sakızlı kek")
elif num == 6:
    print("sifon")
elif num ==7:
    print("dondurma ama çilekli")
elif num == 8:
    print("su")
elif num == 9: 
    print("çiğ kadayıf")
elif num == 10:
    print("peynirli börek ama yufkasız")
else: 
    print("Invalid")
    









"""
name = input("What is your name: ")
age = int(input("How old are you: "))
birth = input("Where did you born: ")
num = int(input("What is your favourite number: "))

if num < 50: 
    print((num * 47 / 16) - (477 / 4) + 42)
elif num > 50: 
    print(num / 12 - 10 * 58 - 200)
else: 
    print("Num is 50")
"""
"""
Q2.  
Get a number from the user and find the modulus of 7. 
Create another number with random from 1 to 50. 
Divide the first number with the second number and do the calculation. 

num . 444 : 16 + 275      12321 + 68779 : 500     49 :16
----------------------- . -------------------- :  -------
140 . 4 + 246 - 16 : 5     510 . 230 - 46 : 12       24


"""
"""
import random 

n = int(input("Enter a number: "))
res = n % 7

ran = random.randint(1,50)

num = res / ran

print((num * 444 / 16 + 275) / (140 * 4 + 246 - 16 / 5) * (12321 + 68779 / 500) / (510 * 230 - 46 / 12) / (49 / 16) / 24)
"""

"""
Q3. 
Using random function, create a number between -100 to 1000. 
If the random number is less than 0, do the calculation. 

num % 23 . 3^7 + 26 
-------------------
      25 + 44

If the number is more than 0, do the calculation. 

57 + 48 . 16 : num - 27 : 5 - 8 . 44
------------------------------------
                3 + 4
                
print the result. 


"""
import random

num = random.randint(-1,1)
if (num < 0): 
    print((num % 23 * 3**7 + 26) / (25 + 44))
else:
    print((57 + 48 * 16 / num - 27 / 5 - 8 * 44) / (3+4))
    

