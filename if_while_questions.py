#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:45:05 2021

@author: berkayakdag
"""

"""

Q1. Ask the height and weight from the user and calculate the users BMI(body mass index)
BMI = kg / m**2
IF BMI index is
below 18.5 = Underweight
Between 18.5 to 24.9 = Normal 
Between 24.9 to 29.9 = Owerweight
30 and above = Obese
Print the result. 

"""

kg = float(input("Enter weight in kg: "))
m = float(input("Enter height in m: "))

bmi = kg / m ** 2
if bmi <  18.5:
    print("Underweight ")
elif bmi > 18.5  and bmi < 24.9  : 
    print("Normal ")
elif bmi > 24.9 and bmi < 29.9  :
    print("Overweight ")
else:
    print("Obese ")
    
"""
Q2. Enter this classes student names. Every time a name entered, count the number of students. 
When x is entered print the number of students. 
(Use while   != 'x')
"""
count = 0
name = input("Enter a name: ")
while name != 'x':
    name = input("Enter a name: ")
    count += 1
print(count)

"""
Q3. The user will enter a number. If the number is odd, ask for a second number and sum the numbers. 
If it is even, ask for another number and sum the numbers. After that create a random generator from
1 to the second number and print out a random number in area. 
"""
import random
num1 = int(input("Enter a number: "))
if num1 % 2 == 1:
    num2 = int(input("Enter number 2: "))
    print(num1+num2)
else: 
    num3 = int(input("Enter number 2: "))
    print(random.randint(1, num1+num3))


















"""
Q3. The user will enter a number. If the number is odd, ask for a second number and sum the numbers. 
If it is even, ask for another number and sum the numbers. After that create a random generator from
1 to the second number and print out a random number in area. 
"""

      
    


