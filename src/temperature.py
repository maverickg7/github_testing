#! /usr/bin/env python

"""This is a python module that converts temperature  
"""

def f_to_k(temp):
    converted = ((temp-32.0)*(5.0/9.0)) + 273.15
    return converted

def k_to_c(temp):
    return temp - 273.15

def f_to_c(temp):
    temp_k = f_to_k(temp)
    temp_c = k_to_c(temp_k)
    return temp_c 

print(f_to_k(32))
print(f_to_k(212))
print(k_to_c(273.15))
print(f_to_c(32.0))
