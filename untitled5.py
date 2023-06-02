# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:36:20 2023

@author: Lenovo
"""
from functools import reduce

def two_number_add(num1,num2):
    add=num1*num2
    return add
def main():
    inputt=list(map(int,input().split()))
    print(reduce(two_number_add,inputt))

if __name__ == "__main__":
    main()
    