#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:43:02 2021

@author: berkayakdag
"""

"""
In a country, the population grows %5 in every year.
This country has a current population of 56492888 (56 million 492 thousand 888) as of this year.
How many years will it take to exeed 85 million population?  
After showing the year, print out the population difference as of this year and target year.
"""

year = 2021
pop = 56492888

popdif= 56492888
yeardif = 2021

while pop < 85000000:
    pop *= 1.05
    year += 1

print("This countries population will exeed 85 million in the year of", year)

print("The population difference in the year of", yeardif, "and the year of", year, "is", pop - popdif)

