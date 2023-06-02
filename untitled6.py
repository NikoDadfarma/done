# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:58:23 2023

@author: Lenovo
"""

from functools import reduce

def two_number_add(num1,num2):
    add=num1+num2
    return add
def main():
    input1=int(input())
    input2=int(input())
    print(reduce(two_number_add,list(range(input1,input2+1))))

if __name__ == "__main__":
    main()