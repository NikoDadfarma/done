# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:42:56 2023

@author: Lenovo
"""

def show_employee(name:str,salary:int=9000) :
    print('name is :',name,'the salary is: ',salary)
def main():
    inputName=input()
    inputsalary=input()
    if inputsalary:
        
        show_employee(inputName,int(inputsalary))
    else:
        show_employee(inputName)

if __name__ == "__main__":
    main()
    