#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:21:20 2021

@author: berkayakdag
"""

"""
In a country, the population grows %5 in every year.
This country has a current population of (56 million 492 thousand 888) as of this year.
How many years will it take to exeed 85 million population?  
After showing the year, print out the population difference as of this year and target year.
"""

pop = 56492888
newpop = 56492888
year = 2021

print('PROGRAM IS UP AND RUNNING')

while newpop <= 85000000:
    newpop+= newpop * 5 / 100
    year = year + 1
    

print('Year Is ' ,year)
print('Pop Difference Is ' , newpop - pop)
print(year - 2021)