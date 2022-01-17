#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:02:36 2021

@author: berkayakdag
"""

"""
nüfus artışı
100 m nüfuslu bir ülkede her yıl %2 oranında nüfus artışı oluyor. 
Kullanıcı bir sayı girecek ve bu sayı kadar yıl sonunda nüfus kaç olacak hesapla
"""

population = 100000000
year = int(input("Enter a number: "))

for i in range (1, year):
    population *= 1.02
    
print("The population will be", population, "after", year, "years." )

