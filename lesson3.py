#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:41:59 2021

@author: berkayakdag
"""


print("Hello world!\nBerkay Akdağ \tTab Space")


name = input("what is your name?: ")
print("Nice to meet you", name)

num1 = int(input("Enter a number: "))
num2 = float(input("Enter another number: "))


print(num1 + num2)

"""
int -> tamsayı -> 5 , 55 ,82931371283, -37218 , -3 , 0
float -> ondalıklı sayı -> 3.14 , 327183721.1, -6.5 , 1.3627813
"""

"""
Q1. Ask the user about his/her name, age and favourite film. 
Give answers 
(Nice to meet you ... my name is ...) 
(Our age difference is x) 
(I prefer ... rather than ...)

"""

name = input("What is your name?: ") 
age = int(input("What is your age?: "))
film = input("What is your favourite film?: ")

print("Nice to meet you,", name, "My name is Berkay")
print("Our age difference is: ", abs(27-age))
print("I prefer Shawshank Redemption rather than ", film)



"""
Ask the user about 2 grades. Grade 1 is %40 and grade 2 is %60. Combine them to find the total grades.
"""

grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))

total = grade1 * 0.4 + grade2 * 0.6
print(total)









