#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:40:49 2021

@author: berkayakdag
"""
import random

eski = "pepe"


while (eski != "0"):
    
  
  print(kod)
  
  kodinput = input("")
  
  print(kodinput)
    
  if (kodinput == kod):
    print("yeni şifreni gir:")
    yeni = input("")

    if eski == yeni:
      print("şifreler aynı")
    else:
      print("şifren değişti şifren " + yeni) 
      eski = yeni