# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:19:11 2023

@author: Lenovo
"""

def show_upper_or_lower(name:str) :
    uper=0
    lower=0
    for i in name:
        if i.isupper():
            uper+=1
        elif i.islower():
            lower+=1
    uperlower=[uper,lower]
    return uperlower
    
def main():
    inputName=input()
    new=show_upper_or_lower(inputName)
    print('No. lower case charachter:' ,new[1])
    print('No. upper case charachter: ',new[0])

if __name__ == "__main__":
    main()