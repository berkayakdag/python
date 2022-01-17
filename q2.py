# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
A program will decide if the person should take a jacket and umbrella or not.
The user will enter the weather temperature on the outside.
The user will enter Y if it is raining outside. 
If the weather is below 15 C, the code will tell the user to wear a jacket.
If there is rain on outside, the code will tell the user to get an umbrella.
"""


temp = int(input("Enter the temperature outside: "))
rain = input("Is it raining?: ")


if temp < 15:
    print("You should consider taking a jacket.")
    
else:
    print("It seems like there is no need for a jacket.")


if rain == "Y":
    print("Take an umbrella with you.")
else:
    print("You probably won't need an umbrella.")
    