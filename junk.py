# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:56:56 2024

@author: frost
"""

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)