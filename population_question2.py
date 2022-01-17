#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:59:40 2021

@author: berkayakdag
"""

pop = 100000000
number = int(input('Yıl Sayısını Girin: '))

for i in range(number):
  pop+=pop * 2 / 100
  
  
text = str(number) + ' Yıl Sonra Şehrin Nüfusu ' + str(pop) + ' Kişi Olur'
print(text)
