#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 11:24:34 2021

@author: berkayakdag
"""

"""
Favourite car

Ask the user his/her favourite car
If BMW, print = You won BMW 520i
If Mercedes-Benz = you won E220
If Tofaş = you won Doğan SLX
else = you won simit
"""

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

"""
User deposits money, if the user enters 0, print the total. 
while
Enter amount: 100 
Enter amount: 50
Enter amount: 75
Enter amount: 0

225

"""
res = 0
money = int(input("Enter amount: "))
res = money
while money != 0:
    money = int(input("Enter amount: "))
    res += money    
print(res)

"""
Enter the names of classmates. When the user enters stop, 
print out the number of students in class.

"""

count = 0 
name = input("Enter a name: ")
while name!='stop':
    name = input("Enter a name: ")
    count +=1
print(count)

"""
Question 2: 

    Ask the user a 5 digits number(check it) and print out the last digit of the number.
    Ex: 12233 -> print 3
    41256 -> print 6
  
"""

