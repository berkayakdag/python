#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 09:31:10 2021

@author: berkayakdag
"""

"""
A list is of an ordered collection data type that is mutable which means 
it can be easily modified and we can change its data values and a list 
can be indexed, sliced, and changed and each element can be accessed 
using its index value in the list. The following are the main 
characteristics of a List:

The list is an ordered collection of data types.
The list is mutable.
List are dynamic and can contain objects of different data types.
List elements can be accessed by index number.
"""

list1 = ['mango', 1 ,'strawberry', 3.5 ,'orange', 'apple', 'banana']

print(list1[1] + list1[3])
list1[2] = "mango"
print(list1[2])
print(list1)






"""
A tuple is an ordered and an immutable data type which means 
we cannot change its values and tuples are written in round brackets. 
We can access tuple by referring to the index number inside the square 
brackets.  
The following are the main characteristics of a Tuple:

Tuples are immutable and can store any type of data type.
it is defined using ().
it cannot be changed or replaced as it is an immutable data type.
"""

tuple1 = ('orange', 'apple', 'banana')
print(tuple1)
print(tuple1[1])


"""
An array is a collection of items stored at contiguous memory locations. 
The idea is to store multiple items of the same type together. 
This makes it easier to calculate the position of each element by 
simply adding an offset to a base value, i.e., the memory location 
of the first element of the array (generally denoted by the name 
of the array). 
The following are the main characteristics of an Array:

An array is an ordered collection of the similar data types.
An array is mutable.
An array can be accessed by using its index number.
"""
import array as arr
   

a = arr.array('i', [1, 2, 3])
   

print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
   

b = arr.array('d', [2.5, 3.2, 3.3])


print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
    
    
#dictionary Ex:1
dict0 = {"Brand" : "Ford",
         "Model" : "Focus",
         "Year" : 2014}

print(dict0["Brand"])
    
#dictionary Ex:2
dict1 = {"Class" : "9A1",
        "Name" : "İpek",
        "height" : 1.65
        }

print(dict1["Name"])


"""
In a school there are 3 classes, in every class there are 3 lessons,
Math, Science, Coding.

Each lesson has 2 topics.

Create the structure of each class, lesson and topics. 

print the result.  

"""

dict2 = {"DeliBilim1" : "9A1",
         "DeliBilim2" : "9A2", 
         "DeliBilim3" : "10A1",
         "9A1-1" : "Math",
         "9A1-2" : "Science",
         "9A1-3" : "Coding",
         "9A2-1" : "Math",
         "9A2-2" : "Science",
         "9A2-3" : "Coding",
         "10A1-1" : "Math",
         "10A1-2" : "Science",
         "10A1-3" : "Coding",
         "Math1" : "Topic1", 
         "Math2" : "Topic2",
         "Math3" : "Topic3", 
         "Science1" : "Topic1",
         "Science2" : "Topic2",
         "Science3" : "Topic3",
         "Coding1" : "Topic1",
         "Coding2" : "Topic2",
         "Coding3" : "Topic3",
         }
print(dict2)







#List 
list1 = ["Volvo", "Audi", "BMW", "Tofaş"]
list1[0] = "Seat"
list1.append("Volkswagen")

print(list1) 

#tuple
tup1 = ("Volvo", "Audi", "BMW", "Tofaş")

print(tup1)


#dictionary
dict1 = {"Volvo" : "XC90", 
         "Audi": "A4", 
         "BMW" : "320i", 
         "Tofaş" : "Doğan SLX" }

dict1["Volvo"] = "S60"

print(dict1)
print(dict1["Audi"])
"""
Question:
Create a list of 5 food, 

Chicken
Pasta
Rice
Chocolate Cake
Doner Kebab

Add one more item to the list with append and print the 1st,
3rd and last item. 
Print Todays meal: ...
"""
list1 = ["chicken", "pasta", "rice", "chocolate cake", "doner kebab"]
list1.append("doritos")
print("Todays meal: ", list1[0], list1[2], list1[5])















"""
Create a dictionary of 5 car brands with models. 

Seat Leon
Volkswagen Golf
Audi A3
Volvo V40 
BMW 118i

Bring the models of the dictionary and write them to a list. 
On the list, the models must be alphabetic. 
"""




dict1 = {"Seat" : "Leon", 
         "Volkswagen" : "Golf", 
         "Audi" : "A3", 
         "Volvo" : "V40",
         "BMW" : "118i"
         }

list1 = [dict1["Audi"], 
         dict1["Volkswagen"], 
         dict1["Seat"], 
         dict1["Volvo"], 
         dict1["BMW"] ]

print(list1)
