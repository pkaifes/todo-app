# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:45:22 2024

@author: frost
"""

username = input("Hello! What's your name? ")

print(f"Hello {username}! How are you feeling today?")
print("1. Happy ")
print("2. Stressed ")
print("3. Tired ")

try:
    user_rating = int(input("Choose 1, 2, or 3: "))
    
    match user_rating:
        case 1:
            print(f"That’s great, {username}! Keep streading your joy")
        case 2:
            print(f"Take a deep breath, {username}. You're doing amazing!")
        case 3:
            print(f"Rest up, {username}. Tomorrow is a fresh start!")
    
except ValueError:
    exit("Please select a number")