# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:53:40 2023

@author: Lenovo
"""

def check_string_reflex(string:str):
    returnBool=0
    if string[::-1]==string[::]:
        returnBool=1
    return bool(returnBool)

            
str1=input()
i=check_string_reflex(str1)
print( 'yes' if i==True  else 'no')