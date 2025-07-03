#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 02:19:17 2025

@author: amarino
"""

# My first atmospheric science Python program
# Temperature conversion functions

def cel_to_fah(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def cel_to_kel(celsius):
    """Convert Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Makes functions smarter so they can be more usefull for real life data
def F_to_C(fah):
    if type(fah) == float or type(fah) == int:
        if fah > -150 and fah < 212:  # Reasonable temperature range
            celsius = (fah - 32) * 5/9
            return celsius
        else:
            return "Temperature out of reasonable range"
    else:
        return "Error: Not a number"
